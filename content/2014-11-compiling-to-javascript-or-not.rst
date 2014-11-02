Compiling to Javascript or not?
###############################

:author: Bruce Mitchener, Jr.
:date: 2014-11-10
:category: Development
:tags: JavaScript
:status: draft

JavaScript is commonly seen as a flawed language. It has plenty
of flaws, some of which are more painful than others. One common
way that people deal with these flaws is to use another language
that compiles to JavaScript and to then write their code in that
other language.

At first, this sounds pretty appealing. You get to choose which
of a few languages to use to address your complaints with JavaScript.
Unhappy with the type system? Try out Dart, TypeScript, AtScript, Elm,
or even PureScript. Want a more concise syntax? Perhaps CoffeeScript
is your thing. Do you wish you were using a Lisp? Well, there are lots of
options there as well, starting with ClojureScript or Parenscript.
There are `many choices`_.

My Project
==========

My project involves creating a platform for building tools that is
based on `Atom Shell`_ and uses a plug-in model to allow users to
extend the core platform.

I also have some requirements:

* I need access to things that will be coming in future versions
  of JavaScript (and fairly soon). An example of this is support
  for working with 64 bit integers (a firm requirement).
* Given that we have a single deployment platform (Atom Shell,
  with a known version of the Chromium browser and the V8 JavaScript
  engine), it would be nice to be able to take advantage of
  developments as they occur.
* Users will be able to enter code within the application and
  have it run. This means that the compiler needs to be able
  to be distributed (easily) with the application and invoked
  on arbitrary user code.
* I don't want to limit people's options too much in how they
  produce their plug-ins. If someone wants to develop their
  plug-in in a language that compiles to JavaScript, it would
  be ideal if they could do so, as long as that language
  provides for sufficient interoperability.

Downsides?
==========

I think that the upsides to compiling from another language
to JavaScript are fairly well known and understood.

However, when evaluating whether or not to use an alternative
language to compile to JavaScript or rather to write directly
in JavaScript now, it seems there are a lot of potential downsides.

Keeping up with JavaScript
--------------------------

JavaScript is constantly evolving. In fact, I am counting on and
relying upon that evolution, given that I need some features
in the future that aren't even specified yet (like decent support
for 64 bit integers).

Using ES6 features isn't possible yet in many languages that
compile to JavaScript. Some support ES3, some support ES5. Adding
to this difficulty is that the decisions for what to support and
when may not be something that is done in the open or on a short
time frame.

The extent to which this matters in a language depends upon the
extent to which the language differs from JavaScript versus being
some form of sugar for JavaScript. For example, PureScript would
probably care less about a lot of this, while this is more of an
issue for TypeScript.

Bi-Directional Interoperability?
--------------------------------

...

Loss of Control
---------------

...

Toolchain Support
-----------------

Can the compiler and associated tools be shipped with my application?
Does the compiler produce decent feedback on errors of various sorts?

This is clearly much easier when the compiler is written in or compiles
to JavaScript.

.. _many choices: https://github.com/jashkenas/coffeescript/wiki/list-of-languages-that-compile-to-js
.. _Atom Shell: https://github.com/atom/atom-shell/
