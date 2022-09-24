"""This module defines utility classes for dynamic interpretation of data which
doesn't have a well-specified structure.

Any instance of one of the classes defined in this module will store the given
`data` argument in an instance attribute which is also named `data`. Subclasses
can then implement additional methods to interpret the data, while inheriting
the constructor documentation and some behaviour. However, the data may not be
fully interpreted, yet. In that case, the "end-user" can always use the `data`
attribute to access the underlying raw data directly.

For example, given a subclass of `DictData` which interprets the `name` field
of any given data in a `dict`:

>>> class NamedItem(DictData):
...     @property
...     def name(self):
...         return self.data['name']

And a subclass of `ListData` which represents any item in the given `list` data
as an instance of the previously defined class `NamedItem`:

>>> class NamedItemList(ListData):
...     @property
...     def __item_class__(self):
...         return NamedItem

We can now construct an instance of `NamedItemList` which interprets the given
data to some extend while ignoring any extra data which it doesn't understand:

>>> data = [
...     {'name': 'foo', 'id': 0},
...     {'name': 'bar', 'id': 1},
...     {'name': 'baz', 'id': 2},
... ]
>>> items = NamedItemList(data)
>>> [item.name for item in items]
['foo', 'bar', 'baz']

However, we can still access the underlying data directly in case we have to:

>>> [item.data['id'] for item in items]
[0, 1, 2]

Thankfully, without having to write any additionaly documentation, the help
output for our subclasses already includes the constructor documentation of
the base class:

>>> def help_output(obj):
...     from contextlib import redirect_stdout
...     from io import StringIO
...
...     captured_stdout = StringIO()
...
...     with redirect_stdout(captured_stdout):
...        help(obj)
...
...     return captured_stdout.getvalue()
>>> '__init__(self, data: dict)' in help_output(NamedItem)
True
>>> '__init__(self, data: list)' in help_output(NamedItemList)
True
"""

from abc import ABC, abstractmethod


class DictData:
    """Represents interpreted data in a `dict`."""

    def __init__(self, data: dict):
        """Stores a reference to the given data for dynamic interpretation at a
        later time.

        The given raw data can be retrieved (and manipulated) at any time using
        the `data` instance attribute.
        """
        self.data = data


class ListData(ABC):
    """Represents interpreted data in a `list`."""

    def __init__(self, data: list):
        """Stores a reference to the given data for dynamic interpretation at a
        later time.

        The given raw data can be retrieved (and manipulated) at any time using
        the `data` instance attribute.
        """
        self.data = data

    def __len__(self):
        return self.data.__len__()

    def __iter__(self):
        return (self.__item_class__(item) for item in self.data.__iter__())

    def __getitem__(self, i):
        return self.__item_class__(self.data.__getitem__(i))

    @property
    @abstractmethod
    def __item_class__(self):
        pass


if __name__ == '__main__':
    import doctest

    doctest.testmod()
