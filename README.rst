=================
attribute-mapping
=================

``attribute-mapping`` is a minimalistic python library to allow
attribute lookups in dictionaries and other mappings.

Compared to many other implementations of the same idea, going by
names such as ``AttrDict`` and various others, this library is
extremely minimal and free of cruft:

- Almost no API

- ``AttributeMapping`` instances do not pretend to be a ``dict``

- Can be used with ``dict`` as well as other objects implementing the
  ``collections.abc.Mapping`` abstract base class

- No restrictions on key/attribute names

- No unpleasant surprises in behaviour or weird corner cases

- Modern code; Python 3.4+ only

- 100% test coverage


Installation
============

::

    python -m pip install attribute-mapping


Usage
=====

Make an ``AttributeMapping`` instance by passing a dictionary or
another mapping::

    from attribute_mapping import AttributeMapping

    d = {"a": 1, "b": {"c": 2, "d": 3}}
    x = AttributeMapping(d)

Now you can access the contents using attribute lookups::

    x.a  # gives 1
    x.b.c  # gives 2

    x.foo = 123
    hasattr(x, "foo")  # True
    del x.foo

In addition to attribute access, subscription (``__getitem__`` and
friends) and containment checks (``in``) also work::

    x["a"]  # gives 1
    x["b"]["c"]  # gives 2
    x["foo"] = 123
    "foo" in x  # True
    del x["foo"]

However, there are *no* other dict-like methods or reserved names, so
you can happily use attributes like ``keys`` and ``items``::

    x.items = [1, 2, 3]

Iteration yields ``(key, value)`` tuples, just like ``.items()`` on
normal mappings would do::

    for key, value in x:
        ...

Finally, to obtain the original object that was used for the
``AttributeMapping``, use the built-in ``vars()`` function::

    d = {"a": 1}
    x = AttributeMapping(d)
    vars(x) is d  # True


Credits
=======

This library is written by wouter bolsterlee (wbolster).

There are a gazillion similar implementations, so the author thanks
the whole Python community for the inspiration to make yet another
implementation of this idea.


Version history
===============

* 1.2.0 (2019-03-12)

  * Add support for (in)equality tests

* 1.1.0 (2019-03-09)

  * Add support for custom mappings

* 1.0.0 (2019-03-08)

  * Initial release


License
=======

BSD; see LICENSE file for details.
