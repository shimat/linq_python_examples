from collections.abc import Iterable
from typing import TypeVar
import more_itertools


T = TypeVar('T')


def single(iterable: Iterable[T]) -> T:
    it = iter(iterable)
    result = next(it)
    try:
        next(it)
    except StopIteration:
        return result
    raise ValueError("Iterable has more than one item")


# single
data1 = ["A"]
data2 = ["A", "B", "C"]
data3 = []

#print(more_itertools.one(data1))
#print(more_itertools.one(data2))
#print(more_itertools.one(data3))
#print(single(data1))
#print(single(data2))
#print(single(data3))

# single_or_default
data1 = ["A"]
data2 = ["A", "B", "C"]
data3 = []

print(more_itertools.only(data1))
#print(more_itertools.only(data2))
print(more_itertools.only(data3))


