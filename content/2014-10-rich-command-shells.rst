Rich Command Shells
###################

:author: Bruce Mitchener, Jr.
:date: 2014-10-10
:category: Development
:tags: Textual Interfaces

Many applications benefit from a mix of a graphical and textual interface.
This has ranged from entire environments, like the Lisp Machine and the
follow-on Common Lisp Interface Manager (CLIM), to specific applications
like Mathematica and others which employ a "notebook interface". There
have also been various attempts at producing richer terminal applications
which can work with either standard or specialized applications to produce
richer, more interactive output. Graphically enhanced textual interfaces
have also found their place in various genres of games over the years.

In our case, we're interested in enhancing the interaction between a
user and a specific tool. We'll take a look here at some of the ideas
that have come before to get an idea of what people have already done
to inform what we do for ourselves.

Some of the things discussed here are old, some are new. Some are long
lost and forgotten (one link below is to archive.org) while others are
actively being worked on today.

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

A shorter, more `concise description`_, might be:

    A presentation is an association between

    * a type of object,
    * an instance of that type of object,
    * and that object's visual representation.

    Or more specifically, when output is done as a presentation, CLIM
    creates an output record associated with an object and a presentation
    type, and saves that record in the window's output history.

The capabilities of CLIM can be, perhaps, be illustrated more clearly:

.. class:: img-polaroid
.. figure:: /static/images/command-shell-lisp-listener.png
   :align: center
   :alt: CLIM listener screenshot

   A screenshot of the `CLIM Listener from Wikipedia`_.

You can see in this screenshot that commands such as ``Show Directory``
and ``Show Class Subclasses`` can have rich output. The extent of the
interaction possible isn't on display in the screenshot.  (It also
shows the presence of inline completion helpers like ``(pathname)``
and ``(class)``, but that's just part of the nice command parser system
present in CLIM.

What did CLIM get right? CLIM provided:

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

Notebook interfaces are interactive documents that represent the
history of commands that have been run within a session. They can
usually be saved, replayed, and shared with other people. Notebook
interfaces typically support rich multimedia, including code with
syntax highlighting, mathematical formulas, graphs, charts, and
formatted text.

`Mathematica`_ was one of the early pioneers in this area.  A simple
screenshot doesn't do Mathematica justice. Try to find the
time to watch Mathematica `in action`_ during the Strange Loop 2014
keynote by Stephen Wolfram. It really is something to be seen.

.. class:: img-polaroid
.. figure:: /static/images/command-shell-mathematica.gif
   :align: center
   :alt: Mathematic screenshot

   Mathematica's Notebook interface

The `iPython`_ implementation is open source, widely used and now
supports multiple languages, not just Python.

The iPython notebook interface can be used with multiple front-ends:

.. class:: img-polaroid
.. figure:: /static/images/command-shell-ipython-terminal.png
   :align: center
   :alt: iPython in terminal screenshot

   iPython running in a terminal

.. class:: img-polaroid
.. figure:: /static/images/command-shell-ipython-notebook.png
   :align: center
   :alt: iPython in web browser screenshot

   iPython using a web browser to display the notebook

iPython 2.0 adds support for `interactive widgets`_

Terminals
---------

Long ago, terminals could do much more exciting things than they do
today.  They supported various graphics protocols for rendering bitmap
and vector graphics.

Check out `libsixel`_ and `PySixel`_ for some examples of what can be done
with `Sixel`_ graphics. The terminal emulators `mlterm`_ and `Tanasinn`_
support this (among others).  gnuplot and netpbm support Sixel output:

.. class:: img-polaroid
.. figure:: /static//images/command-shell-sixel-gnuplot.png
   :align: center
   :alt: libsixel screenshot

   Image from `libsixel`_

As an aside, it looks like `Saitoha`_ is on a personal mission to spread support
for Sixel graphics and has done a lot of work in this area. That's awesome
dedication!

`iTerm2`_ supports embedding images as can be `seen here`_. `Terminology`_
also supports embedding images and other media.

Rich Terminal Applications
--------------------------

There have been many interesting attempts to provide a rich terminal
application for working with the Unix shell, especially with the
advent of the web browser. An early example of a browser-backed shell
was `XMLterm`_. Since then, there has also been `TermKit`_, which has
since passed away. The author of `XMLterm`_ now works on `GraphTerm`_.

While these are all interesting in their own ways, they are not terribly
useful for the type of application that we're looking to build. These
tend to assume that you're creating a new ecosystem surrounding replacing
the Unix shell experience.

.. class:: img-polaroid
.. figure:: /static/images/command-shell-graphterm-ssh-plot.png
   :align: center
   :alt: GraphTerm screenshot

   An example GraphTerm screenshot

Textual Game Interfaces
-----------------------

For now, this is mainly worth mentioning as a curiosity. I have no good
links to point to examples of this. Many games in the 1980s and early
1990s had text input interfaces while the game itself would display
graphics.

Some of the richest textual interfaces that I saw however were in some of
the programmable MUDs, like `LambdaMOO`_ and similar systems. In these,
the entire interface was both programmable and text-based. However,
some systems supported early hypertext-capable clients such as `Pueblo`_,
`TkMOO-light`_ (with a plug-in) and research systems like `Jupiter`_,
the `Jupiter Windowing system`_ and `TWin`_ (which ran on top of out
an out-of-band client/server communication protocol known as `MCP`_).

There was a lot of interesting work in this area, much of it largely
lost to the sands of time.

I found an old screenshot of a game client that we did with IE, a
custom control for talking to the game server, and a whole lot of JavaScript
and CSS back in 2002 or 2003:

.. class:: img-polaroid
.. figure:: /static/images/command-shell-grendels-revenge.png
   :align: center
   :alt: Grendel's Revene screenshot

Another interesting aspect of textual interfaces in games is that they
often required some formatting of the text itself. In some MOO and the
Cold system that I mentioned above, we had a markup language for text
that let us control how it was output for various terminal types. (In
Cold, we supported plain telnet, ANSI text, HTML, Pueblo, and a couple
of other custom outputs, like the screenshot from Grendel's Revenge
above.) In Cold, we could provide links, various layout options
(definition lists, bullet lists, tables, etc.) and the system would
handle making sure everything looked good, that ANSI codes were
used where appropriate, or that the right HTML tags were rendered.

Nowadays, one might use Markdown, ReStructuredText or other things
to achieve some of the same effects, but not everything is possible
with those.

For a simple example from the Cold help system, this markup::

    {p}Nodes from this point down are for core subsystem
    documentation and documentation on specific objects.
    {p}
    {dl columned:
      {dt: {b:{link node=$help_index_subsystem:Subsystem}}}
      {dd: Subsystems Index}
      {dt: {b:{link node=$help_index_objects:Object}}}
      {dd: Core Objects Index}}

Would render in plain text as::

    Nodes from this point down are for core subsystem documentation and
    documentation on specific objects.

            [Subsystem]            Subsystems Index
            [Object]               Core Objects Index

This sort of thing is very useful in a command shell for things
like help text, formatted paragraphs, proper line wrapping,
optionally displaying colored text, etc.

Others
------

We've just taken a brief look at a few different enriched textual
user interfaces. There are surely many others or many details not covered
above. I encourage you to write about them in your own blog posts!

I'll write soon about some applications that I'm working on and how
we might be able to build upon some of the ideas that have come before
as well as how we can take advantage of some of what exists today.

.. _Presentation Based User Interfaces: ftp://publications.ai.mit.edu/ai-publications/pdf/AITR-794.pdf
.. _Common Lisp Interface Manager: http://en.wikipedia.org/wiki/Common_Lisp_Interface_Manager
.. _CLIM specification: http://bauhh.dyndns.org:8000/clim-spec/23-1.html
.. _concise description: http://www.kantz.com/clim-primer/presentation-types.htm
.. _CLIM Listener from Wikipedia: http://en.wikipedia.org/wiki/File:Listener.png
.. _Mathematica: https://reference.wolfram.com/language/tutorial/UsingANotebookInterface.html
.. _iPython: http://ipython.org/
.. _interactive widgets: http://nbviewer.ipython.org/github/ipython/ipython/blob/master/examples/Interactive%20Widgets/Index.ipynb
.. _in action: http://www.youtube.com/watch?v=EjCWdsrVcBM
.. _libsixel: https://github.com/saitoha/libsixel
.. _PySixel: https://github.com/saitoha/PySixel
.. _Sixel: http://en.wikipedia.org/wiki/Sixel
.. _mlterm: https://bitbucket.org/arakiken/mlterm
.. _Tanasinn: http://zuse.jp/tanasinn/
.. _Saitoha: http://saitoha.github.io/
.. _iTerm2: https://github.com/gnachman/iTerm2
.. _seen here: http://www.iterm2.com/images.html
.. _Terminology: https://www.enlightenment.org/p.php?p=about/terminology
.. _XMLterm: http://www.xml.com/pub/a/2000/06/07/xmlterm/
.. _TermKit: https://github.com/unconed/TermKit
.. _GraphTerm: https://github.com/mitotic/graphterm
.. _LambdaMOO: http://en.wikipedia.org/wiki/LambdaMOO
.. _Pueblo: http://pueblo.sourceforge.net/pueblo/
.. _TkMOO-light: http://www.awns.com/tkMOO-light/
.. _Jupiter: http://ftp.lambda.moo.mud.org/pub/MOO/papers/JupiterAV.ps
.. _Jupiter Windowing system: http://ftp.lambda.moo.mud.org/pub/MOO/papers/JupiterWin.ps
.. _TWin: http://web.archive.org/web/*/http://tchat.research.att.net/
.. _MCP: http://www.moo.mud.org/mcp2/
