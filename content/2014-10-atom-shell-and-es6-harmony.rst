Atom Shell and ES6 Harmony
##########################

:author: Bruce Mitchener, Jr.
:date: 2014-10-19
:category: Development
:tags: atom-shell

When building an application using the `Atom Shell`_, you may want to
take advantage of newer Javascript features from `ES6 (Harmony)`_ like
arrow functions, generators, ``for ... of`` loops and many other things
which are not enabled in the V8 Javascript engine by default.

Fortunately, enabling this is pretty easy!

.. code-block:: javascript

    app.on('ready', function() {
      app.commandLine.appendSwitch('js-flags', '--harmony');
      ...
    }

When starting up your Atom Shell application, you can append switches
to the command line that will be given to the embedded Chromium browser
engine.

Note that if you have an incorrect flag being passed, the other flags
that you set may be ignored, so keep an eye on this as you update to
newer versions of Atom Shell as the valid flags may have changed.

Unfortunately, it can be confusing figuring out which version of V8
is being used and what ES6 features are available. As of the time
of this writing, Atom Shell 0.18.1 is using a Chromium 38 and so
it falls in between the Chromium 37 and 39 columns on this
`compatibility chart`_. (But don't look at the Node Harmony column
for figuring out what Atom Shell supports!)

.. _Atom Shell: https://github.com/atom/atom-shell
.. _ES6 (Harmony): https://github.com/atom/atom-shell
.. _compatibility chart: http://kangax.github.io/compat-table/es6/
