"""Demo entry point: run ``python -m lab3``."""

from lab3.countdown import Countdown
from lab3.counter import Counter
from lab3.figure import Circle, Figure, Rectangle, total_perimeter
from lab3.singleton import Application, SingletonMeta
from lab3.temperature import Temperature


def main() -> None:
    """Print results of every variant task."""
    print("Medium tasks")
    figures: list[Figure] = [Rectangle(3, 4), Circle(1)]
    print("total_perimeter ->", total_perimeter(figures))
    counter = Counter(start=10, step=3, min_value=0)
    counter.increment()
    counter.increment()
    print("Counter value ->", counter.get_value())
    print("list(Countdown(3)) ->", list(Countdown(3)))

    print("Advanced tasks")
    first = Application("demo")
    second = Application("demo")
    print("same Application instance ->", first is second)
    SingletonMeta.reset_instances(Application)
    fresh = Application("fresh")
    print("new instance after reset ->", fresh is not first)
    temperature = Temperature(100)
    print("100 C in Fahrenheit ->", temperature.fahrenheit)
    temperature.fahrenheit = 32
    print("32 F in Celsius ->", temperature.celsius)


if __name__ == "__main__":
    main()
