"""Task 1 (advanced): Singleton pattern implemented with a metaclass."""

from typing import Any


class SingletonMeta(type):
    """Metaclass that keeps one instance per concrete class.

    Instances are stored in a class-level cache keyed by the class
    being created, so unrelated singleton classes never share an
    object.
    """

    _instances: dict[type, Any] = {}

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        """Return the cached instance, creating it on first call.

        Later constructions ignore ``args`` and ``kwargs``: the
        object created by the very first call is returned as is.

        Returns:
            The single instance bound to ``cls``.
        """
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

    @classmethod
    def reset_instances(cls, *classes: type) -> None:
        """Forget cached singleton instances.

        Without arguments the whole cache is dropped; otherwise only
        the listed classes are removed. The next construction of a
        dropped class creates a fresh object. Intended for tests.

        Args:
            *classes: singleton classes whose cached instance should
                be deleted; unknown classes are ignored.
        """
        if not classes:
            cls._instances.clear()
            return
        for target in classes:
            cls._instances.pop(target, None)


class Application(metaclass=SingletonMeta):
    """Example singleton representing a running application.

    Two constructions of ``Application`` return the same object; the
    constructor body runs once, on the first construction only.
    """

    def __init__(self, name: str = "app") -> None:
        """Store the application name.

        Args:
            name: name recorded on the first construction; arguments
                of subsequent constructions are ignored.
        """
        self.name = name
        self.starts = 1
