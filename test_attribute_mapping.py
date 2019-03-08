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


def test_special_attributes():
    d = {"foo": "bar"}
    x = AttributeMapping(d)
    assert x.__class__ is AttributeMapping
    assert x.__dict__ is d
