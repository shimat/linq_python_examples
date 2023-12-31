import itertools
from collections.abc import Iterable


def foo(numbers: Iterable[int]) -> None:
    first_3 = itertools.islice(numbers, 3)  # Take(3)
    next_3 = itertools.islice(numbers, 3, 6)  # Skip(3).Take(3)

    print(list(first_3))
    print(list(next_3))


foo(range(10))
foo(x for x in range(10))
