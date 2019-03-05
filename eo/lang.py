"""
EO lang spec.
"""

class Immutable(type):
    """ Immutable object metaclass """
    def __new__(mcs, class_name, bases, class_dict):
        instance = type.__new__(mcs, class_name, bases, class_dict)
        instance.__setattr__ = Immutable._setattr_impl
        instance.__delattr__ = Immutable._delattr_impl
        return instance

    def __call__(cls, *args, **kwargs):
        obj = type.__call__(cls, *args, **kwargs)
        obj.__immutable__ = True
        return obj

    @staticmethod
    def _setattr_impl(obj, attr, value):
        if '__immutable__' in obj.__dict__ and obj.__immutable__:
            raise AttributeError("Set not supported! '{self}' is immutable".format(self=obj))
        object.__setattr__(obj, attr, value)

    @staticmethod
    def _delattr_impl(obj, attr):
        raise AttributeError("Delete not supported! '{self}' is immutable".format(self=obj))


class EO(metaclass=Immutable):
    """
    Base Elegant Object
    """
    def __value__(self):
        raise NotImplementedError("__value__ should be implemented")

    def __call__(self, *args, **kwargs):
        return self.__class__(*args, **kwargs)

    def __bool__(self):
        return bool(EO._unwrap(self))

    def __eq__(self, other):
        return EO._unwrap(self) == EO._unwrap(other)

    def __neg__(self):
        return -EO._unwrap(self)

    def __int__(self):
        return int(EO._unwrap(self))

    def __float__(self):
        return float(EO._unwrap(self))

    def __str__(self):
        return str(EO._unwrap(self))

    def __repr__(self):
        return repr(EO._unwrap(self))

    def __add__(self, other):
        return EO._unwrap(self) + EO._unwrap(other)

    @staticmethod
    def _unwrap(obj):
        if hasattr(obj, '__value__') and callable(obj.__value__):
            return EO._unwrap(obj.__value__())
        return obj
