"""Tests for the Countdown iterator task."""

import unittest

from lab3.countdown import Countdown


class CountdownTests(unittest.TestCase):
    """Checks for :class:`Countdown`."""

    def test_yields_from_start_down_to_zero(self) -> None:
        """Every value from ``start`` down to ``0`` is produced."""
        self.assertEqual(list(Countdown(3)), [3, 2, 1, 0])

    def test_zero_start(self) -> None:
        """A zero start yields only zero."""
        self.assertEqual(list(Countdown(0)), [0])

    def test_object_is_its_own_iterator(self) -> None:
        """``iter()`` returns the very same object."""
        counter = Countdown(2)
        self.assertIs(iter(counter), counter)

    def test_exhausted_instance_keeps_stopping(self) -> None:
        """After ``StopIteration`` every further call stops too."""
        counter = Countdown(1)
        self.assertEqual(next(counter), 1)
        self.assertEqual(next(counter), 0)
        with self.assertRaises(StopIteration):
            next(counter)
        with self.assertRaises(StopIteration):
            next(counter)
        self.assertEqual(list(counter), [])

    def test_iteration_resumes_between_calls(self) -> None:
        """Manual ``next()`` calls continue where they stopped."""
        counter = Countdown(3)
        self.assertEqual(next(counter), 3)
        self.assertEqual(next(counter), 2)
        self.assertEqual(list(counter), [1, 0])

    def test_negative_start_rejected(self) -> None:
        """A negative start raises ``ValueError``."""
        with self.assertRaises(ValueError):
            Countdown(-1)


if __name__ == "__main__":
    unittest.main()
