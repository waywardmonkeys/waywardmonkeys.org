Building A Rich Command Shell
#############################

:author: Bruce Mitchener, Jr.
:date: 2014-10-20
:category: Development
:tags: Textual Interfaces
:status: draft

Previously, I wrote about some existing examples of `Rich Command Shells`_,
some from the past, some from the present.

Now, I'd like to look at this from the practical side of things. I have some
software that I would like to see have a rich command shell.

What do I Want?
===============

First up, what should we consider to be characteristics of a "rich command
shell" for the purposes of this post?

For my interests, I want to see:

* Works in a regular terminal.
* Also works in terminals with more advanced features.
* Adapts to the size and capabilities of the terminal, although I recognize
  that feature negotiation doesn't work for everything, so some things
  will be controlled by settings.
* Works when not run in a terminal (like having output piped to a file or
  another process).
* Can be run in conjunction with a more specialized program that might
  present an even richer interface or embed the functionality somehow.

The shorter version of this is:

* It should work like things to do today, in the existing environment.
* It should adaptively support richer means of interaction as well without
  violating typical assumptions of today.
* The means of adaptation should be flexible and allow progressively
  richer output and interaction models.

This might be boring to some people. They may want to replace the "everything
is a stream of bytes" model of Unix. They may want to replace all existing
terminals with something that supports full HTML and related technologies
or be able to assume that all terminals support some sort of inline media
display.

On the other hand, this might be reassuring to some people who would
otherwise be afraid that "rich command shell" was going to mean the tools
have a GUI, require a mouse, and are no longer scriptable or whatever.

The world evolves slowly and moves in fits and starts, and I'm fine with
that.

.. _Rich Command Shells: http://waywardmonkeys.org/2014/10/10/rich-command-shells/
