import pytest
from attribute_mapping import AttributeMapping


def test_attribute_mapping():

    d = {"a": 1, "b": {"c": 2, "d": 3}}
    ad = AttributeMapping(d)

    assert ad.a == 1
    assert ad.b
    assert ad.b.c == 2

    assert ad["a"] == 1
    assert ad.b["d"] == 3

    with pytest.raises(AttributeError):
        ad.nonexistent

    with pytest.raises(KeyError):
        ad["nonexistent"]

    assert vars(ad) == d
    assert vars(ad) is d

    ad.foo = 123
    assert ad.foo == 123
    ad["foo"] = 456
    assert ad.foo == 456

    assert hasattr(ad, "foo")
    assert "foo" in ad
    del ad.foo
    assert not hasattr(ad, "foo")
    assert "foo" not in ad
    ad.foo = 123
    del ad["foo"]
    assert not hasattr(ad, "foo")
    assert "foo" not in ad


def test_nested_instance():
    a = AttributeMapping({})
    a.foo = AttributeMapping({})
    a.foo.bar = 1
    expected = "AttributeMapping({'foo': {'bar': 1}})"
    assert repr(a) == expected
