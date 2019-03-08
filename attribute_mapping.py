import collections as _collections


class AttributeMapping:
    def __init__(self, d):
        if not isinstance(d, _collections.abc.Mapping):
            raise TypeError("not a mapping")
        object.__setattr__(self, "__dict__", d)

    def __getattribute__(self, name):
        # __dict__ and __class__ are the only special attributes
        # https://docs.python.org/3/reference/datamodel.html#the-standard-type-hierarchy
        if name == "__dict__":
            return object.__getattribute__(self, "__dict__")
        elif name == "__class__":
            return type(self)
        try:
            value = self[name]
        except KeyError as exc:
            raise AttributeError(exc.args[0]) from None
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
        d = object.__getattribute__(self, "__dict__")
        return d[key]

    def __setitem__(self, name, value):
        d = object.__getattribute__(self, "__dict__")
        d[name] = value

    def __delitem__(self, name):
        d = object.__getattribute__(self, "__dict__")
        del d[name]

    def __contains__(self, name):
        try:
            self[name]
        except KeyError:
            return False
        else:
            return True

    def __iter__(self):
        d = object.__getattribute__(self, "__dict__")
        yield from d.items()

    def __repr__(self):
        d = object.__getattribute__(self, "__dict__")
        return "{}({!r})".format(type(self).__name__, d)
