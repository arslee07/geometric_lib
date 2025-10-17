"""A set of formulas for circle."""

import math


def area(r: int | float) -> float:
    """Get circle area.

    The following formula is used: S = pi * r^2, where S is the returned result and pi is a constant.

    Args:
        r: Circle radius.

    Returns:
        Square area.
    """

    return math.pi * r * r


def perimeter(r: int | float) -> float:
    """Get circle perimeter.

    The following formula is used: P = 2 * pi * r,  where P is the returned result and pi is a constant.

    Args:
        r: Circle radius.

    Returns:
        Square area.
    """

    return 2 * math.pi * r
