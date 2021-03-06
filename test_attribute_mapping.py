import collections

import pytest

from attribute_mapping import AttributeMapping


def test_get_original():
    d = {}
    x = AttributeMapping(d)

    assert vars(x) == d
    assert vars(x) is d


def test_constructor_invalid():
    with pytest.raises(TypeError):
        AttributeMapping(123)


def test_attributes():
    d = {"a": 1, "b": {"c": 2, "d": 3}}
    x = AttributeMapping(d)

    assert x.a == 1
    assert x.b
    assert x.b.c == 2

    with pytest.raises(AttributeError):
        x.nonexistent

    x.foo = 123
    assert x.foo == 123
    assert hasattr(x, "foo")

    del x.foo
    assert not hasattr(x, "foo")

    with pytest.raises(AttributeError):
        del x.nonexistent


def test_items():
    d = {"a": 1, "b": {"c": 2, "d": 3}}
    x = AttributeMapping(d)

    assert x["a"] == 1
    assert x.b["d"] == 3

    with pytest.raises(KeyError):
        x["nonexistent"]

    x["foo"] = 456
    assert x["foo"] == 456
    assert "foo" in x

    del x["foo"]
    assert "foo" not in x


def test_nested_instance():
    x = AttributeMapping({})
    x.foo = AttributeMapping({})
    x.foo.bar = 1
    assert vars(x) == {"foo": {"bar": 1}}


def test_repr():
    x = AttributeMapping({"foo": {"bar": 1}})
    expected = "AttributeMapping({'foo': {'bar': 1}})"
    assert repr(x) == str(x) == expected


def test_iteration():
    d = {"foo": "bar"}
    x = AttributeMapping(d)
    for key, value in x:
        assert key == "foo"
        assert value == "bar"

    d = {"a": 1, "b": 2}
    x = AttributeMapping(d)
    assert sorted(x) == [("a", 1), ("b", 2)]


def test_length():
    d = {"a": 1, "b": 2}
    x = AttributeMapping(d)
    assert len(x) == 2
    x.c = 3
    assert len(x) == 3


def test_special_attributes():
    d = {"foo": "bar"}
    x = AttributeMapping(d)
    assert x.__class__ is AttributeMapping
    assert x.__dict__ is d


def test_equality():
    d1 = {"a": "aa"}
    d2 = {"a": "aa"}
    d3 = {"b": "b"}

    assert AttributeMapping(d1) == AttributeMapping(d1)
    assert AttributeMapping(d1) != d1
    assert AttributeMapping(d1) == AttributeMapping(d2)
    assert AttributeMapping(d1) != AttributeMapping(d3)


class MyCustomMapping(collections.abc.Mapping):
    def __getitem__(self, key):
        if key == "a":
            return "aa"
        if key == "b":
            return "bb"
        raise KeyError

    def __iter__(self):
        yield "a"
        yield "b"

    def __len__():
        return 2


def test_custom_mapping():
    m = MyCustomMapping()
    x = AttributeMapping(m)
    assert x.a == "aa"
    assert x.b == "bb"
    with pytest.raises(AttributeError):
        x.c
