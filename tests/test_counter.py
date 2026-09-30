"""Tests for the Counter class task."""

import unittest

from lab3.counter import Counter


class CounterTests(unittest.TestCase):
    """Checks for :class:`Counter`."""

    def test_default_start_and_step(self) -> None:
        """A fresh counter starts at zero and moves by one."""
        counter = Counter()
        self.assertEqual(counter.get_value(), 0)
        counter.increment()
        self.assertEqual(counter.get_value(), 1)
        counter.decrement()
        self.assertEqual(counter.get_value(), 0)

    def test_custom_start_and_step(self) -> None:
        """The step controls both directions."""
        counter = Counter(start=10, step=3)
        counter.increment()
        self.assertEqual(counter.get_value(), 13)
        counter.decrement()
        self.assertEqual(counter.get_value(), 10)

    def test_reset_restores_start(self) -> None:
        """Reset returns the counter to its initial value."""
        counter = Counter(start=5, step=2)
        counter.increment()
        counter.increment()
        self.assertEqual(counter.get_value(), 9)
        counter.reset()
        self.assertEqual(counter.get_value(), 5)

    def test_decrement_below_min_value_rejected(self) -> None:
        """Dropping below ``min_value`` raises ``ValueError``."""
        counter = Counter(start=0, step=2, min_value=-1)
        with self.assertRaises(ValueError):
            counter.decrement()
        self.assertEqual(counter.get_value(), 0)

    def test_non_positive_step_rejected(self) -> None:
        """A zero or negative step raises ``ValueError``."""
        with self.assertRaises(ValueError):
            Counter(step=0)

    def test_start_below_min_value_rejected(self) -> None:
        """The initial value may not violate the bound."""
        with self.assertRaises(ValueError):
            Counter(start=-5, min_value=0)


if __name__ == "__main__":
    unittest.main()
