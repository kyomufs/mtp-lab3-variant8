"""Tests for the Figure class task."""

import math
import unittest

from lab3.figure import Circle, Figure, Rectangle, total_perimeter


class FigureBaseTests(unittest.TestCase):
    """Checks for the abstract :class:`Figure` base class."""

    def test_area_is_not_implemented(self) -> None:
        """The base class refuses to compute an area."""
        with self.assertRaises(NotImplementedError):
            Figure().area()

    def test_perimeter_is_not_implemented(self) -> None:
        """The base class refuses to compute a perimeter."""
        with self.assertRaises(NotImplementedError):
            Figure().perimeter()


class RectangleTests(unittest.TestCase):
    """Checks for :class:`Rectangle`."""

    def test_area(self) -> None:
        """Area equals width multiplied by height."""
        self.assertEqual(Rectangle(3, 4).area(), 12)

    def test_perimeter(self) -> None:
        """Perimeter equals twice the sum of the sides."""
        self.assertEqual(Rectangle(3, 4).perimeter(), 14)

    def test_non_positive_side_rejected(self) -> None:
        """A zero or negative side raises ``ValueError``."""
        with self.assertRaises(ValueError):
            Rectangle(0, 4)


class CircleTests(unittest.TestCase):
    """Checks for :class:`Circle`."""

    def test_area(self) -> None:
        """Area equals ``pi * radius ** 2``."""
        self.assertAlmostEqual(Circle(2).area(), math.pi * 4)

    def test_perimeter(self) -> None:
        """Perimeter equals the circumference."""
        self.assertAlmostEqual(Circle(1).perimeter(), 2 * math.pi)

    def test_non_positive_radius_rejected(self) -> None:
        """A zero or negative radius raises ``ValueError``."""
        with self.assertRaises(ValueError):
            Circle(-1)


class TotalPerimeterTests(unittest.TestCase):
    """Checks for the polymorphic :func:`total_perimeter`."""

    def test_mixed_figures(self) -> None:
        """Rectangles and circles are summed uniformly."""
        figures = [Rectangle(3, 4), Circle(1)]
        self.assertAlmostEqual(
            total_perimeter(figures), 14 + 2 * math.pi
        )

    def test_empty_sequence(self) -> None:
        """An empty sequence gives ``0.0``."""
        self.assertEqual(total_perimeter([]), 0.0)


if __name__ == "__main__":
    unittest.main()
