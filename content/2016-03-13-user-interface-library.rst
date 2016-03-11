What I want in a user interface library
#######################################

:author: Bruce Mitchener, Jr.
:date: 2016-03-13
:category: Development
:tags: Thinking Out Loud, Workbench
:status: draft

It seems like it is always impossible to find what I want. I apparently
want too much.

So, what am I looking for? These are just my own personal desires and
I certainly don't expect that everyone will agree with them.

Requirements
============

* React
* TypeScript
* Documentation
* ARIA attributes
* Theming
* Internationalization / localization

React
-----

I'm planning to use React in my rendering layer, so it would be nice if
the user interface framework that I use has solid support for React.
This seems like a no-brainer.  That said, there is another layer in my
architecture which describes user interfaces and that is what gets
lowered or converted to the actual widget definitions. In theory, this
means that multiple view layers could exist (perhaps even using something
like React Native). But for the start, I need solid React support.

TypeScript
----------

Much like my desire for React support, I am writing my code in TypeScript.
That doesn't mean that the UI *has* to be in TypeScript, but it would
make it more convenient. Otherwise, typing definition files (`.d.ts`)
would need to be maintained and kept up to date. This can be done for
a framework that already exists, but will always be something of a
maintenance burden.

I enjoy the additional reliability that I get in my code from using
TypeScript, and I'd like to get that same additional reliability in
the libraries and frameworks that I depend upon.

Documentation
-------------

Fortunately, with the widespread availability of component library
pages that are full of examples, documentation is much more readily
available today than in the past.

ARIA Attributes
---------------

Having an application be accessible seems like a good goal to have.
This means providing ARIA attributes on our widgets and generated
HTML.

Theming
-------

Everyone wants theming these days. Even better is theming that lets
someone customize the look and feel of a framework fairly easily
without having to modify each and every widget. There are a lot
of approaches that are being taken with this in the React world
including css-modules and inline styles. I don't know how I want to
see this solved in my UI framework of choice, just that I do
want to see it have integrated theming support throughout.

As part of theming, I'm hoping that the default look and feel isn't
trying to mimic a given platform as that never ends up working out
very well.

Internationalization / localization
-----------------------------------

In addition to supporting localized display of numbers, dates,
and other information, all text messages should be localized.
Like theming, this is something that needs to be built into
the framework in a consistent and comprehensive way.

What's out there?
=================

As far as I have been able to find, there are no open source
frameworks that make me happy.

* Material UI
* React-Photonkit
* Ant Design

... Write about each of the above and others ...
