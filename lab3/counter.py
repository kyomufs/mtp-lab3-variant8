"""Task 8 (medium): counter with increment, decrement and reset."""


class Counter:
    """Integer counter that moves up and down by a fixed step.

    The current value is read with the :meth:`get_value` method (a
    ``property`` belongs to a separate advanced task).
    """

    def __init__(
        self,
        start: int = 0,
        step: int = 1,
        min_value: int | None = None,
    ) -> None:
        """Store the initial value, the step and the optional floor.

        Args:
            start: value the counter begins and resets to.
            step: amount added by :meth:`increment` and subtracted
                by :meth:`decrement`.
            min_value: optional lower bound; ``None`` means no bound.

        Raises:
            ValueError: if ``step`` is not positive, or ``start`` is
                already below ``min_value``.
        """
        if step <= 0:
            raise ValueError("step must be positive")
        if min_value is not None and start < min_value:
            raise ValueError("start must not be below min_value")
        self._start = start
        self._step = step
        self._min_value = min_value
        self._value = start

    def get_value(self) -> int:
        """Return the current value of the counter."""
        return self._value

    def increment(self) -> int:
        """Increase the value by ``step``.

        Returns:
            The value after the increase.
        """
        self._value += self._step
        return self._value

    def decrement(self) -> int:
        """Decrease the value by ``step``.

        Returns:
            The value after the decrease.

        Raises:
            ValueError: if the result would be below ``min_value``;
                the current value stays unchanged in that case.
        """
        candidate = self._value - self._step
        if self._min_value is not None and candidate < self._min_value:
            raise ValueError("value would drop below min_value")
        self._value = candidate
        return self._value

    def reset(self) -> int:
        """Restore the initial ``start`` value.

        Returns:
            The restored value.
        """
        self._value = self._start
        return self._value
