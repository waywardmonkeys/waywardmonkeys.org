Querying OS Information
#######################

:author: Bruce Mitchener, Jr.
:date: 2016-03-01
:category: Development
:tags: Workbench
:status: draft

For a project that I'm working on, I would like to be able to retrieve
information from the OS about a variety of things:

* File system
* Current processes running
* Process memory maps
* Open file handles in a process
* File attributes
* File type, mime type
* ... and a lot more!

Some of these are very easy and are just a set of calls to POSIX functions.
Others are highly dependent on the underlying platform.

I want to be able to access this data from an application that is either
running natively or from within node.js when using Electron. I want it on
a minimum of Mac OS X, Linux, FreeBSD and Windows. Support for other
platforms such as NetBSD would be nice.

I don't want this to be very large. The overall code required is likely to
be fairly small. Hopefully, a large number of dependencies would not be
brought in by using a library that provides this information.

I want the data in `JSON-LD`_ format. This is JSON, but with some additional
fields, like ``@type``, that help my application present the data correctly.
It would be nice if there were a way to subset the data such that some of it
wouldn't even be computed. This could be done via a query language ala SQL
or `GraphQL`_.

osquery
-------

Someone suggested that I look into Facebook's `osquery`_ project. On the
surface, it looked very interesting. It supports using SQL to query a
lot of data from the operating system and can encode the results as JSON.

Unfortunately, I don't think that I can use it.

The largest problem is that isn't a library that I can simply use from within
another application, it is intended to run as a separate daemon process
and communicates with client applications over Thrift. This is ideal for the
use cases that *osquery* is designed for, but less ideal for me.

Also, *osquery* is quite large and includes a lot of additional libraries
and functionality: Google's flag and log libraries, some Boost libraries,
Apache Thrift and RocksDB.

Another complication is that the platform support in *osquery* is limited
to Linux, Mac OS X and unofficial support for FreeBSD. There is no support
yet for Windows. The wide range of functionality makes a complete port to
Windows more difficult.

It would be nice if the JSON output from *osquery* could include JSON-LD
metadata, but that also means deciding and standardizing on that metadata.

What path forward?
------------------

I am not sure if it is worth contacting the *osquery* upstream about my
concerns. They have a product that they're happy with and are continuing
to develop. My concerns and requirements don't exactly match up against
theirs. And maybe that's fine!

... Add more here about GraphQL and other things ...


.. _JSON-LD: http://json-ld.org/
.. _GraphQL: http://graphql.org/
.. _osquery: https://osquery.io/
