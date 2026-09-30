"""Tests for the Singleton pattern task."""

import unittest

from lab3.singleton import Application, SingletonMeta


class Service(metaclass=SingletonMeta):
    """Second singleton class used to check class isolation."""

    def __init__(self) -> None:
        """Mark the instance as constructed."""
        self.constructed = True


class SingletonTests(unittest.TestCase):
    """Checks for :class:`SingletonMeta` and :class:`Application`."""

    def tearDown(self) -> None:
        """Drop cached instances created by a test."""
        SingletonMeta.reset_instances(Application, Service)

    def test_two_references_are_the_same_object(self) -> None:
        """Repeated constructions return one identical object."""
        first = Application("first")
        second = Application("other")
        self.assertIs(first, second)

    def test_constructor_runs_once(self) -> None:
        """Arguments of later constructions are ignored."""
        first = Application("first")
        Application("second")
        self.assertEqual(first.name, "first")
        self.assertEqual(first.starts, 1)

    def test_different_classes_get_different_instances(self) -> None:
        """Two singleton classes never share a cached object."""
        application = Application()
        service = Service()
        self.assertIs(Application(), application)
        self.assertIs(Service(), service)
        self.assertIsNot(application, service)

    def test_reset_creates_a_fresh_instance(self) -> None:
        """After a reset the next call builds a new object."""
        first = Application()
        SingletonMeta.reset_instances(Application)
        second = Application()
        self.assertIsNot(first, second)

    def test_reset_without_arguments_clears_everything(self) -> None:
        """A global reset affects all singleton classes."""
        application = Application()
        service = Service()
        SingletonMeta.reset_instances()
        self.assertIsNot(Application(), application)
        self.assertIsNot(Service(), service)

    def test_reset_ignores_unknown_classes(self) -> None:
        """Resetting a plain class raises no error."""
        SingletonMeta.reset_instances(dict)
        self.assertIsNotNone(Application())


if __name__ == "__main__":
    unittest.main()
