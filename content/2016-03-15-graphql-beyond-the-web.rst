GraphQL beyond the Web
######################

:author: Bruce Mitchener, Jr.
:date: 2016-03-15
:category: Development
:tags: Thinking Out Loud, Workbench

`GraphQL`_ is (from their site):

    DECLARATIVE
        Query responses are decided by the client rather than the
        server. A GraphQL query returns exactly what a client asks
        for and no more.

    COMPOSITIONAL
        A GraphQL query itself is a hierarchical set of fields. The
        query is shaped just like the data it returns. It is a natural
        way for product engineers to describe data requirements.

    STRONG-TYPED
        A GraphQL query can be ensured to be valid within a GraphQL
        type system at development time allowing the server to make
        guarantees about the response. This makes it easier to build
        high-quality client tools.

The `GraphQL`_ website has a lot of additional information, documentation,
and some initial implementations.

I'm going to assume that you're at least roughly familiar with it, but
as a quick example, this query:

.. code:: javascript

   {
     hero {
       id
       name
       friends {
         id
         name
       }
     }
   }

This query could return something like:

.. code:: javascript

   {
     "data": {
       "hero": {
         "id": "2001",
         "name": "R2-D2",
         "friends": [
           {
             "id": "1000",
             "name": "Luke Skywalker"
           },
           {
             "id": "1002",
             "name": "Han Solo"
           },
           {
             "id": "1003",
             "name": "Leia Organa"
           }
         ]
       }
     }
   }

A simpler query over the same data that is parameterized might look like:

.. code:: javascript

   query FetchSomeIDQuery($someId: String!) {
     human(id: $someId) {
       name
     }
   }

And a response from that, given a value of ``1000`` for ``$someId`` would be:

.. code:: javascript

   {
     "data": {
       "human": {
         "name": "Luke Skywalker"
       }
     }
   }

This gives a very rough idea of what GraphQL can look like and a brief
demonstration of how the query can determine the "shape" of the data
that is returned.

Beyond the Web
==============

When I saw GraphQL, I started thinking about how this could improve some
other systems that I work with.

LLDB
----

For example, I have been working with `LLDB`_ off and on over the last
year and a half. The code involved in getting some data about the
current threads and their stacks is somewhat tedious:

.. code:: python

  for thread_idx, thread in enumerate(process):
    for frame_idx, frame in enumerate(thread):
      function = frame.GetFunctionName()
      function_name = frame.GetFunctionName() or ''
      address = frame.GetPCAddress().GetLoadAddress(target)
      module = frame.GetModule().GetFileSpec().GetFilename()
      file_name = frame.GetLineEntry().GetFileSpec().GetFilename()
      line_number = frame.GetLineEntry().GetLine()

Each of these calls crosses from Python into LLDB. This creates
a pretty big surface area for the API, that while flexible, is
pretty substantial. Additionally, some times a request to LLDB
for data might involve a call over IPC (or even RPC) to the
``lldb-server`` or the actual process that is being debugged.

This makes managing responsiveness and delays in updating a
user interface more cumbersome (chained promises, etc).

Querying OS Information
-----------------------

For another project, I discussed in a `recent post`_, how I'd like
to be able to make queries against the underlying OS for things like
process lists, open file handles, process memory maps and a lot more.

Rather than a traditional API, I would find it useful to be able
to get back a bunch of JSON.

Some of the information that my application needs is very specific
to a particular view, so just getting *everything* back in a JSON
blob isn't ideal. Some information is more expensive to gather and
maintain, again making getting everything at once less than ideal.

But I also don't want a traditional API where I have to get data
piece by piece.

GraphQL?
--------

GraphQL seems to be an interesting option to improve the developer
experience here.

A query against LLDB to fetch a bunch of information about current
threads and stack frames might look like:

.. code:: javascript

   {
     thread {
       id
       name
       frames {
         id
         name
         pc-address
         function {
           address
           name
           module {
             name
           }
           file_name
           line_number
         }
       }
     }
   }

This would allow LLDB to optimize this however it likes to avoid
round trips. From the perspective of the developer working with
LLDB, it would be a single request that returns with all of the
relevant data.  LLDB could even send this query over the wire to
the ``lldb-server`` to avoid even more overhead.

It also feels like it would be an API simplification, for the
parts that are associated with querying for data.

On the OS introspection side of things, a GraphQL query for
the current process list might just be:

.. code:: javascript

   {
     process {
       pid
       ppid
       command
       time
       mem
     }
   }

A more detailed view of the process list or a highly detailed
view of a single process would modify that query to fetch the
data that they need.

Only JSON?
==========

One concern that is commonly voiced is "What if I don't want JSON?"

Perhaps you want data in your own efficient encoding like `msgpack`_
or `CBOR`_ or directly into your application structures.  Perhaps you
are running with a JS engine in the same process and want to directly
create the JS engine's objects rather than first constructing some
JSON and then parsing it.

For this, I think it would be a good idea to have a ``value_builder``
interface that can be implemented by the calling application and
passed along with a query. The interface should probably be event-based
like SAX parsers of old, so that it has functions like ``start-object``,
``start-array``, ``start-object``, ``start-key``, ``end-object``, and
so on. This API could expose a richer type system than JSON natively
offers.

An Update
=========

`Kamil Rytarowski`_, a NetBSD hacker, has decided to write a library
called `netquery`_ which will hopefully allow the sort of OS queries
that I want to see. This should be a great opportunity to experiment
with `GraphQL`_ beyond the web.

I look forward to contributing to `netquery`_.

.. _GraphQL: http://graphql.org/
.. _LLDB: http://lldb.llvm.org/
.. _recent post: http://waywardmonkeys.org/2016/03/07/querying-os-information/
.. _msgpack: http://msgpack.org/
.. _CBOR: http://cbor.io/
.. _Kamil Rytarowski: https://github.com/krytarowski
.. _netquery: https://github.com/krytarowski/netquery
