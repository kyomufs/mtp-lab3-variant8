"""Tests for the Temperature property task."""

import unittest

from lab3.temperature import ABSOLUTE_ZERO_CELSIUS, Temperature


class CelsiusPropertyTests(unittest.TestCase):
    """Checks for the :attr:`Temperature.celsius` property."""

    def test_getter_returns_stored_value(self) -> None:
        """The constructor value is readable through the getter."""
        self.assertEqual(Temperature(25).celsius, 25)

    def test_setter_updates_value(self) -> None:
        """Assigning through the property replaces the value."""
        temperature = Temperature(25)
        temperature.celsius = -10
        self.assertEqual(temperature.celsius, -10)

    def test_absolute_zero_is_allowed(self) -> None:
        """The boundary value itself is valid."""
        temperature = Temperature(0)
        temperature.celsius = ABSOLUTE_ZERO_CELSIUS
        self.assertEqual(temperature.celsius, -273.15)

    def test_below_absolute_zero_rejected(self) -> None:
        """Anything colder raises ``ValueError`` on set and init."""
        temperature = Temperature(0)
        with self.assertRaises(ValueError):
            temperature.celsius = -300
        with self.assertRaises(ValueError):
            Temperature(-500)


class FahrenheitPropertyTests(unittest.TestCase):
    """Checks for the two-way :attr:`Temperature.fahrenheit`."""

    def test_fahrenheit_is_derived_from_celsius(self) -> None:
        """The getter applies the standard conversion formula."""
        self.assertAlmostEqual(Temperature(100).fahrenheit, 212)
        self.assertAlmostEqual(Temperature(0).fahrenheit, 32)

    def test_setter_converts_back_to_celsius(self) -> None:
        """Storing Fahrenheit updates the Celsius value."""
        temperature = Temperature(0)
        temperature.fahrenheit = 212
        self.assertAlmostEqual(temperature.celsius, 100)
        self.assertAlmostEqual(temperature.fahrenheit, 212)

    def test_below_absolute_zero_rejected(self) -> None:
        """A Fahrenheit value below absolute zero raises."""
        temperature = Temperature(0)
        with self.assertRaises(ValueError):
            temperature.fahrenheit = -500

    def test_both_views_stay_in_sync(self) -> None:
        """Changing Celsius immediately changes Fahrenheit."""
        temperature = Temperature(0)
        temperature.celsius = 100
        self.assertAlmostEqual(temperature.fahrenheit, 212)


if __name__ == "__main__":
    unittest.main()
