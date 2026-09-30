"""Task 8 (advanced): Temperature class built on ``property``."""

ABSOLUTE_ZERO_CELSIUS: float = -273.15


class Temperature:
    """Temperature with Celsius and Fahrenheit property views.

    Celsius is the single stored value; Fahrenheit is always derived
    from it, so both views stay in sync automatically.
    """

    def __init__(self, celsius: float = 0.0) -> None:
        """Store a temperature given in degrees Celsius.

        Args:
            celsius: initial temperature; assignment goes through the
                :attr:`celsius` setter and is validated.

        Raises:
            ValueError: if ``celsius`` is below absolute zero.
        """
        self.celsius = celsius

    @property
    def celsius(self) -> float:
        """Current temperature in degrees Celsius."""
        return self._celsius

    @celsius.setter
    def celsius(self, value: float) -> None:
        """Validate and store a Celsius temperature.

        Args:
            value: temperature in degrees Celsius.

        Raises:
            ValueError: if ``value`` is below ``-273.15``.
        """
        if value < ABSOLUTE_ZERO_CELSIUS:
            raise ValueError(
                f"temperature {value} C is below absolute zero"
            )
        self._celsius = value

    @property
    def fahrenheit(self) -> float:
        """Current temperature in degrees Fahrenheit."""
        return self._celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value: float) -> None:
        """Store a Fahrenheit temperature by converting it to Celsius.

        Args:
            value: temperature in degrees Fahrenheit.

        Raises:
            ValueError: if the converted value is below absolute
                zero (below ``-459.67`` F).
        """
        self.celsius = (value - 32) * 5 / 9
