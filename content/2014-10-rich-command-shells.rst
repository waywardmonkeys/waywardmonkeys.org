Rich Command Shells
###################

:author: Bruce Mitchener, Jr.
:date: 2014-10-08
:category: Development
:tags: Polymer, ProjectX
:status: draft

Many applications benefit from a mix of a graphical and textual interface.
This has ranged from entire environments, like the Lisp Machine and the
follow-on Common Lisp Interface Manager (CLIM), to specific applications
like Mathematica and others which employ a "notebook interface". There
have also been various attempts at producing richer terminal applications
which can work with either standard or specialized applications to produce
richer, more interactive output. Graphically enhanced textual interfaces
have also found their place in various genres of games over the years.

In our case, we're interested in enhancing the interaction between a
user and a specific tool. So we'll take a look at some of the previous
work in this area and then a brief look at some of our requirements in
the context of two separate projects, one public, one not yet public.

A Look Back
===========

Common Lisp Interface Manager
-----------------------------

Like many things, early research into graphically enhanced and interactive
textual interfaces was carried out within the Lisp world. An early paper
`Presentation Based User Interfaces`_ by Eugene C. Ciccarelli IV at MIT
from 1984 laid the groundwork for something called "presentations". This
was further evolved as part of Dynamic Windows on the Symbolics Lisp
Machine, and then carried over into the `Common Lisp Interface Manager`_.

From the `CLIM specification`_:

    The core around which the CLIM application user interface model is
    built is the concept of the application-defined user interface data
    type. Each application has its own set of semantically significant
    user interface entities; a CAD program for designing circuits has
    kits various kinds of components (gates, resistors, and so on), while
    a database manager has its relations and field types. These entities
    have to be displayed to the user (possibly in more than one displayed
    representation) and the user has to be able to interact with and
    specify the entities via pointer gestures and keyboard input. Frequently
    each user interface entity has a corresponding Lisp data type (such as
    an application-specific structure or CLOS class definition), but this
    is not always the case. The data representation for an interaction entity
    may be a primitive Lisp data type. In fact, it is possible for several
    different user interface entities to use the same Lisp data type for
    their internal representation, for example, building floor numbers
    and employee vacation day totals could both be represented internally
    as integers.

    CLIM provides a framework for defining the appearance and behavior of
    these user interface entities via the presentation type mechanism. A
    presentation type can be thought of as a CLOS class that has some
    additional functionality pertaining to its roles in the user interface
    of an application. By defining a presentation type the application
    programmer defines all of the user interface components of the entity:


    * Its displayed representation, textual or graphical
    * Textual representation, for user input via the keyboard
    * Pointer sensitivity, for user input via the pointer

    In other words, by defining a presentation type, the application
    programmer describes in one place all the information about an
    object necessary to display it to the user and interact with the
    user for object input.

This can be, perhaps, be illustrated more clearly:

.. figure:: /static/images/command-shell-lisp-listener.png
   :align: center

   A screen shot of the `CLIM Listener from Wikipedia`_.

You can see in this screen shot that commands such as ``Show Directory``
and ``Show Class Subclasses`` can have rich output. The extent of the
interaction possible isn't on display in the screen shot.  (It also
shows the presence of inline completion helpers like ``(pathname)``
and ``(class)``, but that's just part of the nice command parser system
present in CLIM.

What did presentations, as shown in CLIM, get right? CLIM provided:

* The ability for a presentation to vary itself according
  to the capabilities of the output device.
* Rich output types, not just text.
* Interactive output via the mouse. Output could be used to fill
  requirements for subsequent commands. (Like selecting a file from
  a previous ``Show Directory`` when prompted for a file.)

CLIM did a lot of things very well and provided a pretty enjoyable
environment within which to work.

Notebook Interfaces
-------------------

...


Rich Terminal Applications
--------------------------

There have been many interesting attempts to provide a rich terminal
application for working with the Unix shell, especially with the
advent of the web browser. An early example of a browser-backed shell
was `XMLterm`_. Since then, there has also been `TermKit`_, which has
since passed away. The author of `XMLterm`_ now works on `GraphTerm`_.

There have also been attempts to provide richer terminal experiences
with `Terminology`_ as well as some patches to iTerm2 to support
a new escape code for embedding graphics data to show in the terminal
window.

While these are all interesting in their own ways, they are not terribly
useful for the type of application that we're looking to build. These
tend to assume that you're creating a new ecosystem surrounding replacing
the Unix shell experience.

Textual Game Interfaces
-----------------------

For now, this is mainly worth mentioning as a curiosity. I have no good
links to point to examples of this. Many games in the 1980s and early
1990s had text input interfaces while the game itself would display
graphics.

Some of the richest textual interfaces that I saw however were in some
the programmable MUDs, like `LambdaMOO`_ and similar systems. In these,
the entire interface was both programmable and text-based. However,
some systems supported early hypertext-capable clients such as `Pueblo`_,
`TkMOO-light`_ (with a plug-in) and research systems like `JupiterMOO`_
and `TWin`_ (which ran on top of out an out-of-band client/server
communication protocol known as `MCP`_).

There was a lot of interesting work in this area, much of it largely
lost to the sands of time.

Others
------

We've just taken a brief look at a few different enriched textual
user interfaces. There are surely many others or many details not covered
above. I encourage you to write about them in your own blog posts!

Our Applications
================

...


.. _Presentation Based User Interfaces: ftp://publications.ai.mit.edu/ai-publications/pdf/AITR-794.pdf
.. _Common Lisp Interface Manager: http://en.wikipedia.org/wiki/Common_Lisp_Interface_Manager
.. _CLIM specification: http://bauhh.dyndns.org:8000/clim-spec/23-1.html
.. _CLIM Listener from Wikipedia: http://en.wikipedia.org/wiki/File:Listener.png
.. _XMLterm: http://www.xml.com/pub/a/2000/06/07/xmlterm/
.. _TermKit: https://github.com/unconed/TermKit
.. _GraphTerm: https://github.com/mitotic/graphterm
.. _Terminology: https://www.enlightenment.org/p.php?p=about/terminology
.. _LambdaMOO: http://en.wikipedia.org/wiki/LambdaMOO
.. _Pueblo: http://pueblo.sourceforge.net/pueblo/
.. _TkMOO-light: http://www.awns.com/tkMOO-light/
.. _JupiterMOO: http://ftp.lambda.moo.mud.org/pub/MOO/papers/JupiterWin.ps
.. _TWin: http://web.archive.org/web/*/http://tchat.research.att.net/
.. _MCP: http://www.moo.mud.org/mcp2/
