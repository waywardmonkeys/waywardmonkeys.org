Looking at Packet Dissection
############################

:author: Bruce Mitchener, Jr.
:date: 2014-10-26
:category: Development
:tags: javascript, networking, dissection

For the project that I am working on (not yet disclosed), I was
thinking that it would be interesting to be able to integrate a
view of what is happening on the network, much like `Wireshark`_
and other tools can provide. The view would be more targeted
towards what the user was doing, but the overall idea would be
the same: capture network traffic and perform some basic analysis
on it to display it visually.

This led to some interesting research, which I've decided to discuss
here! (For those who feel this is a long post, there's a summary
of sorts at the end.)

Capturing Traffic
=================

node_pcap
---------

Given that I'm using `Atom Shell`_ to build this application and that
uses `Node.JS`_, one of my first thoughts was to take a look at
`node_pcap`_. After all, ``node_pcap`` was used successfully in
tools like `htracr`_, so perhaps it would work well here.

Unfortunately, I ran into a series of issues with ``node_pcap``. For
one thing, it wants to run the capture in the same process, and since
performing a capture requires putting the network interface into
promiscuous mode, it requires elevated privileges. I am not comfortable
with the idea that my application would require elevated / Administrator
privileges to run and the security risk seemed high.

Additionally, ``node_pcap`` is native code given that it is interfacing
with a native library. Atom Shell is using the unstable development
version of Node.js, 0.11.x rather than the current stable version of
Node.js, 0.10.x (for good reasons). Unfortunately, the APIs used by
native code to write extensions to Node.js have changed substantially
in the development versions of Node.js (also for good reasons), so
compiling ``node_pcap`` for use in Atom Shell would be problematic
and require work. While there is a project, `nan`_ or "Native Abstractions
for Node.js", which helps simplify this process, it doesn't really
look like ``node_pcap`` is heavily maintained, so it isn't clear
how useful this effort would be in the long run, especially given
the security concerns that I already raised.

That said, there is some interesting code in JavaScript in ``node_pcap``
for tracking TCP states and doing some HTTP processing. We'll come
back to that later.

scapy
-----

Another interesting tool is `scapy`_ which is written in Python. Sadly,
it looks like they forgot how to maintain their own website. In fact,
almost all of the links on this site to anything related to the code
are currently broken.  With some digging, you'll find the `development
site for scapy`_.

Anyway, ``scapy`` is interesting and looks pretty powerful. It would
definitely have to run as a separate process, so some of the security
issues are sorted out already. However, it would mean including enough
of a Python distribution for ``scapy`` to run.

Finally, ``scapy`` is licensed under the GPLv2 license. While this isn't
an issue directly since we'd be running it as a sub-process and not
linked into our codebase, it could be an issue for users down the road
who want to extend part of the system and it complicates licensing which
is otherwise a combination of MIT, BSD and Apache 2 licenses so far
for the most part.

The issue of having to bundle a Python distribution (and having to deal
with that on each platform) is enough of an issue for me to not want
to consider this for now.

Wireshark
---------

`Wireshark`_ has an impressive ecosystem and a lot of support. But it is
less clear to me how to integrate this cleanly. Issues include how to
package it up, the undocumented nature of working with Wireshark as
a library (``libwireshark``), the GPLv2 licensing, and so on.

tcpdump
-------

While very simple, ``tcpdump`` is an appealing option. It is already
present on many hosts for collecting network traffic. For collecting
traffic, I should be able to just run it via a subprocess, using
sudo, and have it output PCAP-formatted binary output and read
that via a pipe.

Parsing PCAP data using JavaScript looks to be pretty straight forward
and in fact, there's already a tool for doing so that integrates
well with Node's streams: `node-pcap-parser`.

This leaves me with no licensing issues, something that works across
Mac OS X, Linux and FreeBSD, and without the security issues of
running my main process with elevated privileges.

Packet Dissection
=================

We're still left with the issue of now needing to dissect the packets
that we're getting via PCAP.

Existing Options
----------------

Again, there are strong options available for inspecting and dissecting
packets like Wireshark and Scapy. And again, many of the same complaints
about them are true. One new complaint can be lodged against Wireshark:
it has a long `history of vulnerabilities`_ due to bugs in parsing and
dissecting packets.

A New Option?
-------------

As we noted before, `node_pcap`_ actually contains some support for
packet inspection. I don't want to use ``node_pcap`` for capturing
traffic for the reasons described before, but perhaps the code
in ``node_pcap`` can be adapted for use in a new project?

Along similar lines, there is the start of a network analyzer in
the `Dylan`_ language called `Network Night Vision`_ which contains
`descriptions of many networking protocols`_. One thing to note about
Network Night Vision is that it uses `binary-data`_ which is a declarative
way to describe how a packet should be parsed from and assembled to a
buffer. This was described in a paper `Secure Networking`_ and
`A domain-specific language for manipulation of binary data in Dylan`_
(presented at ILC 2007).

Interestingly, there are similar binary parser libraries available in
the Node.JS ecosystem. To me, the most interesting one was `binary-parser`_,
in part due to how it generates code to have good performance. Most of
the available options in the Node.JS ecosystem (like `dissolve`_ and
`node-binary`_) are pretty similar in terms of their features and flexibility.

Is there room in the world for a new family of packet dissectors and
a corresponding framework, based on `binary-parser`_? Good question!
Are we reinventing the world? Perhaps. But with some clear goals:

* Cleanly separating packet dissection from capturing traffic so that
  not everything needs to be running with elevated privileges.
* Using a declarative and safe approach to dissection to avoid
  security vulnerabilities due to parsing / dissecting bugs.
* Openly and liberally licensed under an MIT, BSD or Apache 2
  license.

Digging In!
===========

So, let's dig in and see what happens when we actually experiment
with some of the above!

Starting with just launching ``tcpdump`` and getting some packets
seems like a good start:

.. code-block:: javascript

   var sudo = require('sudo');

   tcpdump = sudo(['tcpdump', '-c', '3', '-w', '-', '-U', 'tcp port 80']);
   tcpdump.on('close', function () {
     console.log('tcpdump complete.');
   });
   tcpdump.stdout.on('data'), function(data) {
     console.log('Got some pcap data.');
   });
   tcpdump.stderr.on('data'), function(data) {
     console.log(data.toString());
   });

This is pretty straight forward. Now, we're going to wire it up to
`node-pcap-parser`_:

.. code-block:: javascript

   var sudo        = require('sudo'),
       pcap_parser = require('pcap-parser');

   tcpdump = sudo(['tcpdump', '-c', '3', '-w', '-', '-U', '-i', 'en0', 'tcp port 80']);
   tcpdump.on('close', function () {
     console.log('tcpdump complete.');
   });
   tcpdump.stderr.on('data', function (data) {
     console.log(data.toString());
   });
   parser = pcap_parser.parse(tcpdump.stdout);
   parser.on('packet', function(packet) {
     console.log(packet.header);
     console.log(packet.data);
   });

The differences here are:

* We wire up the ``tcpdump.stdout`` to a PCAP parser and display the
  result of the ``packet`` event rather than a ``data`` event.
* We specify ``-i en0`` in the ``tcpdump`` command line. This is because
  ``tcpdump`` on Mac OS X dumps in pcap-ng format but the parser being
  used here doesn't support that. So, by specifying an interface,
  ``tcpdump`` drops back to the old format which this parser can
  understand.

Now, we can move on and just do quick and dirty IPv4 and TCPv4 parsers
using `binary-parser`_ (it has them as examples), and call them on the
packet data:

.. code-block:: javascript

   parser.on('packet', function(packet) {
     var ip = ipv4Parser.parse(packet.data.slice(14));
     var tcp = tcpv4Parser.parse(ip.payload);
     console.log(ip.payload.slice(tcp.dataOffset * 4).toString());
   });

Since we're just doing this quick and dirty, we carved off the first
14 bytes as they're the Ethernet framing (2 6 byte MAC addresses and
a 2 byte type code).

Notably, we aren't:

* Parsing pcap-ng data like tcpdump emits by default.
* Correctly dealing with anything and are just assuming everything
  is a TCP packet.
* Emitting events so that other things can respond to the traffic.
* Using anything like a nice library structure or dissector
  framework.

But this is a good enough proof of concept. From here, we can address
the above and do something like the TCP and HTTP trackers in
`node_pcap`_.

A Brief Summary
===============

I wasn't happy with some existing solutions for capturing or
dissecting packets for a variety of reasons:

* I didn't want to run the capture in the same process due to the
  security issues involved and needing to run the capture process with
  special or elevated privileges.
* I wanted open and liberal licensing to not complicate the licensing
  of my own product.
* I wanted to minimize the amount of native code involved and the
  complexities of supporting both Node 0.10.x and 0.11.x (required
  for usage in `Atom Shell`_).
* I didn't want to have to bundle / package a distribution of Python
  (on some platforms).
* I wasn't excited by something with a long `history of vulnerabilities`_.
* I want a declarative approach to performing packet dissection.
* I want something that integrates cleanly with JavaScript and the
  model of emitting events.

And it looks like I'll end up creating a framework that meets my
needs, so stay tuned!

.. _Wireshark: http://www.wireshark.org/
.. _Atom Shell: https://github.com/atom/atom-shell/
.. _Node.JS: http://nodejs.org/
.. _node_pcap: https://github.com/mranney/node_pcap
.. _htracr: https://github.com/mnot/htracr
.. _nan: https://github.com/rvagg/nan
.. _scapy: http://www.secdev.org/projects/scapy/
.. _development site for scapy: http://bb.secdev.org/scapy
.. _node-pcap-parser: https://github.com/kunklejr/node-pcap-parser
.. _history of vulnerabilities: http://www.cvedetails.com/vendor/4861/Wireshark.html
.. _Dylan: http://opendylan.org/
.. _Network Night Vision: https://github.com/dylan-hackers/network-night-vision
.. _descriptions of many networking protocols: https://github.com/dylan-hackers/network-night-vision/tree/master/protocols
.. _binary-data: http://opendylan.org/documentation/binary-data/
.. _Secure Networking: http://www.itu.dk/people/hame/secure-networking.pdf
.. _A domain-specific language for manipulation of binary data in Dylan: http://www.itu.dk/people/hame/ilc07-final.pdf
.. _binary-parser: https://github.com/keichi/binary-parser
.. _dissolve: https://github.com/deoxxa/dissolve
.. _node-binary: https://github.com/substack/node-binary
