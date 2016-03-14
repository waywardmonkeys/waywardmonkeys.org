Finding a User Interface library
################################

:author: Bruce Mitchener, Jr.
:date: 2016-03-14
:category: Development
:tags: Thinking Out Loud, Workbench

I'm building something for building developer tools. That's pretty
vague, but I'd like to keep it that way for now. To do this, I
wanted to use an existing user interface library. Unfortunately,
it seems like it is always impossible to find what I want. I apparently
want too much.

My Requirements
===============

So, what am I looking for? These are just my own personal desires and
I certainly don't expect that everyone will agree with them.

**React**
    I'm planning to use `React`_ in my rendering layer, so it would be nice if
    the user interface framework that I use has solid support for React.
    This seems like a no-brainer.  That said, there is another layer in my
    architecture which describes user interfaces and that is what gets
    lowered or converted to the actual widget definitions. In theory, this
    means that multiple view layers could exist (perhaps even using something
    like React Native). But for the start, I need solid React support.

**TypeScript**
    Much like my desire for React support, I am writing my code in `TypeScript`_.
    That doesn't mean that the UI *has* to be in TypeScript, but it would
    make it more convenient. Otherwise, typing definition files (``.d.ts``)
    will need to be maintained and kept up to date.

**Documentation**
    Fortunately, with the widespread availability of component library
    pages that are full of examples, documentation is much more readily
    available today than in the past. But some libraries still try
    to get away without having good documentation or documentation that
    is patchy and inconsistent in quality. World class tools need
    world class documentation.

**Accessibility**
    Having an application be accessible is important. It is important
    to serve disabled users well, but since we're building development
    tools, it is important as many developers enjoy being able to use
    tools without a mouse. In addition to providing `ARIA`_ attributes,
    we will also need to provide rich keyboard navigation for elements
    such as tab widgets, sliders and select boxes.

**Theming**
    Everyone wants theming these days. Even better is theming that lets
    someone customize the look and feel of a framework fairly easily
    without having to modify each and every widget. There are a lot
    of approaches that are being taken with this in the React world
    including css-modules and inline styles. I don't know how I want to
    see this solved in my UI framework of choice, just that I do
    want to see it have integrated theming support throughout.

**Look and Feel**
    Related to theming, I'm hoping that the default look and feel isn't
    trying to mimic a given platform as that never ends up working out
    very well.

**Internationalization / localization**
    In addition to supporting localized display of numbers, dates,
    and other information, all text messages should be localized.
    Like theming, this is something that needs to be built into
    the framework in a consistent and comprehensive way.

**Actively Maintained**
    I don't want to use a library which isn't being actively
    maintained. I'd like to see recent activity, both in terms
    of improvements as well as bug fixes.

**Licensing**
    I prefer fairly open licensing.

Ant Design
==========

As is often the case, my apparent idealism has led me to a place
that I didn't really expect to find myself.

I've looked at several libraries, including, but not limited to:

* Material UI
* React-Photonkit
* Ant Design

In the end, I think that I'm going to go with `Ant Design`_ and
help to evolve it in directions that match my own goals. If that
fails, I can always fork it and build on it.

Ant Design is the work of a team at Alibaba in China.

How well does Ant Design meet my requirements?

**React**

Ant Design is written for React, so there is no issue here.

Ant Design is a re-packaging of a `number of components`_ written by the
same people. These components are available separately (and individually).
They have also been used by other UI frameworks like `UXCore`_. (Interestingly,
UXCore is the work of another team at Alibaba.)

**TypeScript**

While it is not written in TypeScript, it does have a set of typings
available in `DefinitelyTyped`_. This is a new development from the
last couple of weeks.

**Documentation**

Ant Design has documentation for each widget and what properties that
widget has. There are working examples of many of the features provided.
The one issue here is that these are in Chinese, but that hasn't really
been an issue for me yet between Google Translate and viewing the source
of the examples.

**Accessibility**

Ant Design doesn't currently do much with `ARIA`_ attributes. I am
hopeful that this can be improved via pull requests and discussion
with the core team.

It does have some support additional keyboard navigation but further
investigation will be needed in this area.

**Theming**

Ant Design is built with theming in mind, but I haven't investigated
how much theming is supported or how easy it is.

**Look and Feel**

Ant Design has a look of its own. It doesn't try to mimic an
existing platform or vendor. I find it visually appealing.

**Internationalization / localization**

Ant Design has some support for loading messages from locale files
for Chinese and English text. The locale support within Ant Design
supports dynamically changing the language and updating the rendered UI.
This has been improved within the last couple of weeks.

For further localization concerns, there is `an example`_ of it being
integrated with `react-intl`_.

**Actively Maintained**

It is being actively maintained by a commercial entity and is under
active development. To feel out how the maintainers treated the project,
I decided to do an initial pull request.

I filed a bug with a question about moving from usage of ``React.createClass``
to ES2015-style classes that extend ``React.Component``. After an initial
confirmation from them that they were interested, I submitted a partial
patch as a pull request for feedback.

All responses have been prompt, even on weekends. They have been positive
and encouraging. Requests to improve my work have been clear and they
have provided an example of what they mean.

I chose my original issue as it would be an excuse to go through a lot
of the code, but also it was a good signal for how receptive they were
to changes that touched many places within the code from an 'outsider'
as well as how much they value consistency and uniformity within their
code.

**Licensing**

Happily, Ant Design and the underlying components are all MIT licensed.

What Next?
==========

I'm going to continue trying out `Ant Design`_ within my prototypes. I'll
also continue to talk with the upstream about making further improvements
and helping out with improving the code. I'd really like to see the
documentation and some other materials available with an English translation
and I'm interested in helping out with that.

I think that, with some effort to make it more accessible to people who
don't speak Chinese, Ant Design and the underlying React components could
be a pretty interesting framework for many more people than it currently
serves.

.. _React: http://facebook.github.io/react/
.. _TypeScript: http://www.typescriptlang.org/
.. _ARIA: https://www.w3.org/WAI/intro/aria
.. _Ant Design: http://ant.design/docs/react/introduce
.. _number of components: http://react-component.github.io/badgeboard/
.. _UXCore: http://uxco.re/
.. _DefinitelyTyped: https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/antd
.. _an example: https://github.com/ant-design/intl-example
.. _react-intl: https://github.com/yahoo/react-intl
