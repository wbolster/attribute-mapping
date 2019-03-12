import collections as _collections


class AttributeMapping:
    def __init__(self, mapping):
        if not isinstance(mapping, _collections.abc.Mapping):
            raise TypeError("not a mapping")
        object.__setattr__(self, "mapping", mapping)

    def __getattribute__(self, name):
        # __dict__ and __class__ are the only special attributes
        # https://docs.python.org/3/reference/datamodel.html#the-standard-type-hierarchy
        if name == "__dict__":
            return object.__getattribute__(self, "mapping")
        elif name == "__class__":
            return type(self)
        try:
            value = self[name]
        except KeyError as exc:
            raise AttributeError(exc.args[0] if exc.args else name) from None
        if isinstance(value, _collections.abc.Mapping):
            value = AttributeMapping(value)
        return value

    def __setattr__(self, name, value):
        if isinstance(value, type(self)):
            value = vars(value)
        self[name] = value

    def __delattr__(self, name):
        try:
            del self[name]
        except KeyError as exc:
            raise AttributeError(exc.args[0]) from None

    def __getitem__(self, key):
        mapping = object.__getattribute__(self, "mapping")
        return mapping[key]

    def __setitem__(self, name, value):
        mapping = object.__getattribute__(self, "mapping")
        mapping[name] = value

    def __delitem__(self, name):
        mapping = object.__getattribute__(self, "mapping")
        del mapping[name]

    def __contains__(self, name):
        try:
            self[name]
        except KeyError:
            return False
        else:
            return True

    def __iter__(self):
        mapping = object.__getattribute__(self, "mapping")
        yield from mapping.items()

    def __repr__(self):
        mapping = object.__getattribute__(self, "mapping")
        return "{}({!r})".format(type(self).__name__, mapping)

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        mapping = object.__getattribute__(self, "mapping")
        other_mapping = object.__getattribute__(other, "mapping")
        return mapping == other_mapping
