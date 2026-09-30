"""Task 10 (medium): countdown iterator class."""


class Countdown:
    """Iterator counting from ``start`` down to zero.

    The instance is its own iterator: :meth:`__iter__` returns
    ``self``, and :meth:`__next__` yields ``start``, ``start - 1``,
    ..., ``1``, ``0`` and only then raises :class:`StopIteration`.

    State handling: the counter remembers its position between calls,
    so iteration can be paused and resumed with plain ``next()``.
    Once exhausted the instance stays exhausted — every following
    ``next()`` raises :class:`StopIteration` again and the instance is
    never restarted by :meth:`__iter__`. To count down a second time,
    create a new ``Countdown(start)`` object; there is no built-in
    reset method.
    """

    def __init__(self, start: int) -> None:
        """Set the first value of the countdown.

        Args:
            start: non-negative number the countdown begins from.

        Raises:
            ValueError: if ``start`` is negative.
        """
        if start < 0:
            raise ValueError("start must be non-negative")
        self._start = start
        self._next_value: int | None = start

    def __iter__(self) -> "Countdown":
        """Return ``self``: the object is its own iterator."""
        return self

    def __next__(self) -> int:
        """Return the next countdown value.

        Returns:
            The current value, beginning with ``start``.

        Raises:
            StopIteration: when the countdown has reached zero and
                the value ``0`` was already returned; an exhausted
                instance keeps raising it on every further call.
        """
        if self._next_value is None or self._next_value < 0:
            raise StopIteration
        value = self._next_value
        self._next_value -= 1
        return value
