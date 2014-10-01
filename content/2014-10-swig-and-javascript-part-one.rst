SWIG and JavaScript - Part One
##############################

:author: Bruce Mitchener, Jr.
:date: 2014-10-01
:category: Development
:tags: SWIG, JavaScript, ProjectX

I experiment with a lot of ideas for projects and see which ideas stick,
which seem interesting, which require something that I can't provide, etc.

A project that I'm working on now may well be interesting and within
my capabilities and the resources that I can muster, but I don't want to
identify it specifically yet.

Anyway, this project requires using Node.js to talk to a C++ library with
an extensive API. An interesting detail is that this library already has
a solid Python API, built via SWIG.

JavaScript and SWIG
===================

Version 3.0 of `SWIG`_ began to support JavaScript. It supports using
JavaScriptCore or V8 as the JS engine, and Node.js as a specialization
of the V8 support.

For now, I have hacked the SWIG interface files from the C++ library
to wrap Python-specific portions in ``#ifdef SWIG_PYTHON`` so that
they can be shared with JavaScript. In the longer term, should this
project work out and I decide to upstream the changes to support
having JavaScript bindings, I will clean this up and move some things
into separate files for each language in a tidier fashion.

In fairly short order, I was able to get a Node.js module built
that wrapped the library::

    swig -c++ -javascript -node -I../../include -I. -o X_wrap.cxx ../X.swig

Next up was building this for Mac OS X and correctly linking to the
framework for the C++ project. This involved changing the configuration
for ``node-gyp`` in my ``binding.gyp``::

      "conditions": [
        ["OS=='mac'", {
          "xcode_settings": {
            'INSTALL_PATH': '@rpath',
            'LD_DYLIB_INSTALL_NAME': '',
            "OTHER_CPLUSPLUSFLAGS" : ["-std=c++11", "-stdlib=libc++"],
            "MACOSX_DEPLOYMENT_TARGET" : "10.8",
            'OTHER_LDFLAGS': [
              '-Wl,-rpath,@loader_path/../../deps',
              '-F<(module_root_dir)/deps'
            ]
          },
          "link_settings" : { "libraries" : ["X.framework"] }
        }],
        ...

This shows a couple of things:

* I had to set the ``MACOSX_DEPLOYMENT_TARGET`` to ``10.8`` so that
  I would have modern C++ features available as the C++ code relied
  upon things like ``<atomic>``. I may be able to specify ``10.7``,
  but I didn't try.
* I enabled C++11 support and using the ``libc++`` library. There's
  nothing unusual about this when doing work with a C++11 codebase.
* I had to set a ``rpath`` on the binary being built and linked here
  (using ``-Wl,-rpath``) so that it would be able to find the
  framework at run-time. The ``-F`` is to find the framework at
  compile time.

Mac OS X and Run-Paths
======================

On Mac OS X, you'll usually end up wanting to have a good understanding
of rpaths when building frameworks and executables that use them.

Plenty of things have been written about this already:

* `Run-Path Dependent Libraries`_
* `Friday Q&A 2009-11-06: Linking and Install Names`_
* `Using @rpath: Why and How`_

The important thing to know here is that our library needs to know
how to find the framework, so it needs to have a run-path set, and so
we do that.

I'm hoping that with some thought, I might be able to simplify this
in the future.

Node.js and V8 versions
=======================

At this point, I could write a test script that exercised the C++
library and run it via Node.js. Yay!

Unfortunately, my real goal here introduced a new complication.

I don't want to just use this C++ library from a Node.js application.
I actually want to write a GUI for it using `Atom Shell`_. Atom
Shell is an embedded version of the Chrome (Chromium) browser linked
up with Node.js to let you produce standalone applications rather
than a traditional browser application. Unfortunately, this introduces
some complexities into the process.

Atom Shell uses the unstable, development version of Node.js, 0.11.x
rather than the stable 0.10.x. Partly, this is due to the features
that were added to Node.js to support `multiple contexts`_ that Atom
Shell requires. Atom Shell also uses a newer version of the V8
JavaScript engine as that is what Chromium uses. Both the newer
version of Node.js and the updated V8 engine used by Atom Shell are
not API / ABI compatible with Node.js 0.10.x. This now means that
our Swig-wrapped Node.js module as described above doesn't work!

Fortunately, there was a pull request available for SWIG that added
support for newer versions of V8. Unfortunately, V8 doesn't expose
its version information in the header files, so there's no easy
way to figure this out at compile time automatically! What SWIG
has done is to allow you to specify your V8 version number on
the SWIG command line. So, I installed a version of SWIG using that
pull request (which has since been merged), dug up a V8 version
number, and did a new build::

    /opt/swig/bin/swig -c++ -javascript -node -DV8_VERSION=0x032435 \
      -I../../include -I. -o X_wrap.cxx ../X.swig

Next up, we had to make some changes to how we run ``node-gyp`` to
do our actual build, but those were pretty straight forward and are
described in the `Atom docs`_.

Now, we once again had a build of the C++ library, a SWIG-generated
JavaScript / Node.js binding for it, and the ability to load it within
the Atom Shell.

What problems will we run into next? Stay tuned!

.. _SWIG: http://www.swig.org/
.. _Run-Path Dependent Libraries: https://developer.apple.com/library/mac/documentation/DeveloperTools/Conceptual/DynamicLibraries/100-Articles/RunpathDependentLibraries.html
.. _Friday Q&A 2009-11-06\: Linking and Install Names: https://mikeash.com/pyblog/friday-qa-2009-11-06-linking-and-install-names.html
.. _Using @rpath\: Why and How: http://www.dribin.org/dave/blog/archives/2009/11/15/rpath/
.. _Atom Shell: https://github.com/atom/atom-shell
.. _multiple contexts: http://strongloop.com/strongblog/whats-new-node-js-v0-12-multiple-context-execution/
.. _Atom docs: https://github.com/atom/atom-shell/blob/master/docs/tutorial/using-native-node-modules.md#the-node-gyp-way
