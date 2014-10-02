Initial Thoughts on Polymer
###########################

:author: Bruce Mitchener, Jr.
:date: 2014-10-02
:category: Development
:tags: Polymer, ProjectX

I've been doing some web development off and on for many years (since 1996).
I started out in an interpreted language on top of an object database that
was serving up a web-based discussion forum that I was writing and shipping.
I moved on from there to various other tools over the years including various
home-grown templating languages, Django templates, Jinja2 and others. I
helped produce web applications using ExtJS, others using jQuery / jQuery UI,
and experimented with various other frameworks over the years. I've followed
along with what people are doing in ReactJS and related tools like Om.
It is all interesting.

A Recent Project
================

I recently built a web-based UI for a memory / heap profiler for emscripten.
This is just some Jinja2 templates and Flask on the server side. The UI is
using Bootstrap and went through several iterations of various JS tools and
frameworks for handling graphs, grids, and charts.  This was something of
a nightmare (and honestly, the code still is terrible).  Many tools didn't
play well together. Some had issues due to CSS or JS clashing. Others just
wanted to control more than I wanted to let them control. Getting jQuery UI,
Bootstrap, Slick Grid, and other things all playing nicely together in a
single page wasn't entirely fun. And how should I write my new controls /
visualizations / widgets? There wasn't any clearly right answer and given
the lack of an over-arching framework, anything would've involved even more
work, and it wasn't going to be of direct benefit to my client, so I didn't
have the time to do it.

Things are a bit of a mish-mash. It works, but it definitely isn't
pretty on the inside.

An Upcoming Project
===================

For an upcoming project, which I'm just calling ProjectX for now,
I need to build a really solid user interface running inside `Atom
Shell`_ talking to a C++ library via Node.js bindings. This project
needs a strong extensibility mechanism with plugins, including
UI. This is interesting and brings up some questions and possible
requirements.

* Should ProjectX mandate that everyone extending it use a particular
  framework? Some things require that people use ReactJS or Angular
  or Ember or ExtJS or even an entirely different language like
  ClojureScript.
* What should a plugin export? How should others use it? How
  should events and other things be coordinated?
* What is a good widget set to use for building the interface?
  How complete is it? How many other people are working with
  and extending it and perhaps even publishing their own
  widgets?
* I'm almost certainly going to have a number of custom widgets
  that I'll have to make. Should I publish them for others to
  use?
* What options are available to me because I'm using Atom Shell
  and don't have to worry about random browsers out in the field?
  What can I reap from being able to assume a relatively current
  version of the Chromium browser?

Web Components
==============

Having been looking around for the last couple of years to keep
up with the world of web application development, I already
knew that I wouldn't be too happy with many of the solutions
out there. I didn't want to bet everything on Ember or Angular
or frameworks in ClojureScript.

`Web Components`_ though ... Now that sounds interesting!

So, I went and watched `Google I/O 2014 - Polymer and Web Components
change everything you know about Web development`_ and `Google I/O
2014 - Unlock the next era of UI development with Polymer`_ to catch
up with where things were at today.

A bit over a year ago, I had heard about Google's `Polymer Project`_
after Google I/O 2013. This sounded really exciting and interesting,
but it wasn't clear how good the browser support was, whether or
not other browsers would be coming along, whether or not it would
see much uptake in the community, or even whether or not it was
practical or ready for production usage. I decided against using
it as the time on a project due to the massive amount of uncertainty
that I felt.

This project though is going to run in Atom Shell. I don't have to
worry about supporting IE or Safari or even FireFox. Admittedly,
it is still early days for Web Components and the Polymer Project,
but the promise is already visible and it is usable today.

How does this match up with some of the questions raised above?

* Web Components allow people to use what they like within
  a component (within reason). It isn't going to force everyone
  to learn Angular or ClojureScript or ReactJS or some other
  framework. They will have to learn some new technologies,
  but these are technologies designed to assist in inter-operation.
* A plugin can be provided as a set of web components. They
  can use events with the DOM like anything else. They can
  almost feel like native extensions to the browser environment.
* Finding a good widget set still remains to be done. There are
  a couple of options here, from Polymer's "Core" elements to
  Polymer's "Paper" elements to things like Mozilla's "Brick"
  elements. Even Microsoft has publicly experimented with providing
  web components for WinJS. It seems like more and more components
  are being published on a regular basis, so the options available
  are only growing.
* Can I publish my own web components? Sure! (In fact, I'm
  excited enough about being able to do so that I went and
  registered componentfoundry.org and a GitHub organization
  to do so.)
* Atom Shell really helps make this an easier choice. Since
  Atom Shell is using Chromium 37.x (currently), it already
  has full support for the Web Component technologies, so
  I won't need much or any of the polyfill from Polymer. I
  will still be using their "sugaring" layer though.

Admittedly, there will be many things to sort out and figure
out. Can we find a set of elements that look good together
and that integrate well together? Will the promise of component
interoperability come to fruition here? Will highly specialized
components be easy to find or build, like grids that can
hold half a million rows or that integrate charts that use
D3 to render large datasets?

These questions seem to be open issues for pretty much
every framework though, so hopefully the advantages of
Web Components will work out. Perhaps I'll be able to help
push things along by providing some new components.

For the first time in a long while, I'm excited about the
idea of building an application using web technologies
rather than resigned to having to do so!

.. _Atom Shell: https://github.com/atom/atom-shell
.. _Web Components: http://webcomponents.org/
.. _Google I/O 2014 - Polymer and Web Components change everything you know about Web development: http://www.youtube.com/watch?v=8OJ7ih8EE7s
.. _Google I/O 2014 - Unlock the next era of UI development with Polymer: http://www.youtube.com/watch?v=HKrYfrAzqFA
.. _Polymer Project: https://www.polymer-project.org/
