"""Task 4 (medium): Figure base class with area and perimeter."""

import math
from collections.abc import Sequence


class Figure:
    """Base class for geometric figures.

    The base class provides no geometry of its own: :meth:`area` and
    :meth:`perimeter` must be overridden by every concrete subclass.
    """

    def area(self) -> float:
        """Return the area of the figure.

        Raises:
            NotImplementedError: always, the base class is abstract.
        """
        raise NotImplementedError

    def perimeter(self) -> float:
        """Return the perimeter of the figure.

        Raises:
            NotImplementedError: always, the base class is abstract.
        """
        raise NotImplementedError


class Rectangle(Figure):
    """Rectangle defined by its width and height."""

    def __init__(self, width: float, height: float) -> None:
        """Store the two side lengths.

        Args:
            width: length of the horizontal side.
            height: length of the vertical side.

        Raises:
            ValueError: if any side is not positive.
        """
        if width <= 0 or height <= 0:
            raise ValueError("rectangle sides must be positive")
        self.width = width
        self.height = height

    def area(self) -> float:
        """Return the width multiplied by the height."""
        return self.width * self.height

    def perimeter(self) -> float:
        """Return twice the sum of the two side lengths."""
        return 2 * (self.width + self.height)


class Circle(Figure):
    """Circle defined by its radius."""

    def __init__(self, radius: float) -> None:
        """Store the radius.

        Args:
            radius: length of the circle radius.

        Raises:
            ValueError: if the radius is not positive.
        """
        if radius <= 0:
            raise ValueError("circle radius must be positive")
        self.radius = radius

    def area(self) -> float:
        """Return ``pi * radius ** 2``."""
        return math.pi * self.radius**2

    def perimeter(self) -> float:
        """Return the circumference ``2 * pi * radius``."""
        return 2 * math.pi * self.radius


def total_perimeter(figures: Sequence[Figure]) -> float:
    """Return the sum of perimeters of all ``figures``.

    The function is polymorphic: it never checks concrete types,
    every figure computes its own perimeter.

    Args:
        figures: sequence of figures, may be empty.

    Returns:
        The summed perimeter, ``0.0`` for an empty sequence.
    """
    total: float = 0.0
    for figure in figures:
        total += figure.perimeter()
    return total
