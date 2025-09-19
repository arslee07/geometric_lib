"""A set of formulas for rectangle."""

from typing import TypeVar

T = TypeVar("T", int, float)


def area(a: T, b: T) -> T:
    """Get rectangle area.

    The following formula is used: S = a * b

    Args:
        a: Rectangle width.
        b: Rectangle height.

    Returns:
        Rectangle area.
    """

    return a * b


def perimeter(a: T, b: T) -> T:
    """Get rectangle perimeter.

    The following formula is used: P = (a + b) * 2

    Args:
        a: Rectangle width.
        b: Rectangle height.

    Returns:
        Rectangle perimeter.
    """

    return (a + b) * 2
