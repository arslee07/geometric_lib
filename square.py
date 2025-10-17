"""A set of formulas for square."""

from typing import TypeVar

T = TypeVar("T", int, float)


def area(a: T) -> T:
    """Get square area.

    The following formula is used: S = a^2, where S is the returned result.

    Args:
        a: Square side length.

    Returns:
        Square area.
    """

    return a * a


def perimeter(a: T) -> T:
    """Get square perimeter.

    The following formula is used: P = 4 * a, where P is the returned result.

    Args:
        a: Square side length.

    Returns:
        Square perimeter.
    """

    return 4 * a
