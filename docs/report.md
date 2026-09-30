# Отчёт по лабораторной работе №3

Самодуров Матвей Николаевич, группа 221341, вариант 8.

## Средняя сложность

- **№4 Класс «Фигура» (площадь, периметр)** — `lab3/figure.py`:
  базовый класс `Figure` с методами `area()` и `perimeter()`, которые
  по умолчанию бросают `NotImplementedError`, то есть класс работает
  как абстрактный. Подклассы `Rectangle` (ширина/высота) и `Circle`
  (радиус, `math.pi`) переопределяют оба метода. Полиморфизм
  демонстрирует функция `total_perimeter(figures: Sequence[Figure])`:
  она принимает смешанную последовательность объектов и вызывает
  `perimeter()` не проверяя их конкретный тип.
- **№8 Класс-счётчик (увеличение/уменьшение)** — `lab3/counter.py`:
  класс `Counter(start: int = 0, step: int = 1, min_value: int | None = None)`
  хранит текущее значение, `increment()`/`decrement()` двигают его на
  `step`, `get_value()` возвращает значение (обычный метод, а не
  `property` — это отдельное задание повышенной сложности),
  `reset()` возвращает исходное `start`. Если после `decrement()`
  значение оказалось бы ниже `min_value`, бросается `ValueError`,
  причём текущее значение не меняется.
- **№10 Класс-итератор** — `lab3/countdown.py`: класс
  `Countdown(start: int)` реализует протокол итератора — `__iter__`
  возвращает `self`, `__next__` отдаёт `start`, `start - 1`, …, `1`,
  `0` и затем бросает `StopIteration`. Отрицательный `start` даёт
  `ValueError`. Состояние сохраняется между вызовами `next()`, а
  после исчерпания `__next__` продолжает бросать `StopIteration`
  при каждом повторном вызове; возобновить отсчёт можно только новым
  экземпляром — в классе намеренно нет метода сброса (так описано в
  докстринге).

## Повышенная сложность

- **№1 Паттерн Singleton** — `lab3/singleton.py`: метакласс
  `SingletonMeta` хранит кэш экземпляров `dict[type, Any]` и
  переопределяет `__call__`: при первом создании объект строится и
  кладётся в кэш, все последующие обращения возвращают тот же объект
  и игнорируют аргументы конструктора. Разные классы лежат в кэше под
  разными ключами, поэтому не делят экземпляр. Класс `Application`
  с `metaclass=SingletonMeta` — пример singleton-класса. Для тестов
  добавлен `SingletonMeta.reset_instances(*classes)`: удаляет из кэша
  указанные классы (или весь кэш без аргументов), после чего следующее
  создание строит новый объект.
- **№8 Класс с использованием `property`** — `lab3/temperature.py`:
  класс `Temperature` хранит температуру в градусах Цельсия;
  `celsius` — `property` с геттером и сеттером, в сеттере проверка
  `value < -273.15` → `ValueError` (граница допустима, конструктор
  тоже идёт через сеттер). `fahrenheit` — второе `property`,
  двусторонняя связь: геттер вычисляет `C * 9 / 5 + 32`, сеттер
  переводит `F` в `C` и сохраняет через сеттер `celsius`, поэтому
  валидация и синхронизация выполняются в одном месте.

## Проверки

Демонстрация (`uv run python -m lab3`):

```text
Medium tasks
total_perimeter -> 20.283185307179586
Counter value -> 16
list(Countdown(3)) -> [3, 2, 1, 0]
Advanced tasks
same Application instance -> True
new instance after reset -> True
100 C in Fahrenheit -> 212.0
32 F in Celsius -> 0.0
```

Тесты — `uv run python -m unittest discover -s tests -v`:

```text
test_exhausted_instance_keeps_stopping (test_countdown.CountdownTests.test_exhausted_instance_keeps_stopping)
After ``StopIteration`` every further call stops too. ... ok
test_iteration_resumes_between_calls (test_countdown.CountdownTests.test_iteration_resumes_between_calls)
Manual ``next()`` calls continue where they stopped. ... ok
test_negative_start_rejected (test_countdown.CountdownTests.test_negative_start_rejected)
A negative start raises ``ValueError``. ... ok
test_object_is_its_own_iterator (test_countdown.CountdownTests.test_object_is_its_own_iterator)
``iter()`` returns the very same object. ... ok
test_yields_from_start_down_to_zero (test_countdown.CountdownTests.test_yields_from_start_down_to_zero)
Every value from ``start`` down to ``0`` is produced. ... ok
test_zero_start (test_countdown.CountdownTests.test_zero_start)
A zero start yields only zero. ... ok
test_custom_start_and_step (test_counter.CounterTests.test_custom_start_and_step)
The step controls both directions. ... ok
test_decrement_below_min_value_rejected (test_counter.CounterTests.test_decrement_below_min_value_rejected)
Dropping below ``min_value`` raises ``ValueError``. ... ok
test_default_start_and_step (test_counter.CounterTests.test_default_start_and_step)
A fresh counter starts at zero and moves by one. ... ok
test_non_positive_step_rejected (test_counter.CounterTests.test_non_positive_step_rejected)
A zero or negative step raises ``ValueError``. ... ok
test_reset_restores_start (test_counter.CounterTests.test_reset_restores_start)
Reset returns the counter to its initial value. ... ok
test_start_below_min_value_rejected (test_counter.CounterTests.test_start_below_min_value_rejected)
The initial value may not violate the bound. ... ok
test_area (test_figure.CircleTests.test_area)
Area equals ``pi * radius ** 2``. ... ok
test_non_positive_radius_rejected (test_figure.CircleTests.test_non_positive_radius_rejected)
A zero or negative radius raises ``ValueError``. ... ok
test_perimeter (test_figure.CircleTests.test_perimeter)
Perimeter equals the circumference. ... ok
test_area_is_not_implemented (test_figure.FigureBaseTests.test_area_is_not_implemented)
The base class refuses to compute an area. ... ok
test_perimeter_is_not_implemented (test_figure.FigureBaseTests.test_perimeter_is_not_implemented)
The base class refuses to compute a perimeter. ... ok
test_area (test_figure.RectangleTests.test_area)
Area equals width multiplied by height. ... ok
test_non_positive_side_rejected (test_figure.RectangleTests.test_non_positive_side_rejected)
A zero or negative side raises ``ValueError``. ... ok
test_perimeter (test_figure.RectangleTests.test_perimeter)
Perimeter equals twice the sum of the sides. ... ok
test_empty_sequence (test_figure.TotalPerimeterTests.test_empty_sequence)
An empty sequence gives ``0.0``. ... ok
test_mixed_figures (test_figure.TotalPerimeterTests.test_mixed_figures)
Rectangles and circles are summed uniformly. ... ok
test_constructor_runs_once (test_singleton.SingletonTests.test_constructor_runs_once)
Arguments of later constructions are ignored. ... ok
test_different_classes_get_different_instances (test_singleton.SingletonTests.test_different_classes_get_different_instances)
Two singleton classes never share a cached object. ... ok
test_reset_creates_a_fresh_instance (test_singleton.SingletonTests.test_reset_creates_a_fresh_instance)
After a reset the next call builds a new object. ... ok
test_reset_ignores_unknown_classes (test_singleton.SingletonTests.test_reset_ignores_unknown_classes)
Resetting a plain class raises no error. ... ok
test_reset_without_arguments_clears_everything (test_singleton.SingletonTests.test_reset_without_arguments_clears_everything)
A global reset affects all singleton classes. ... ok
test_two_references_are_the_same_object (test_singleton.SingletonTests.test_two_references_are_the_same_object)
Repeated constructions return one identical object. ... ok
test_absolute_zero_is_allowed (test_temperature.CelsiusPropertyTests.test_absolute_zero_is_allowed)
The boundary value itself is valid. ... ok
test_below_absolute_zero_rejected (test_temperature.CelsiusPropertyTests.test_below_absolute_zero_rejected)
Anything colder raises ``ValueError`` on set and init. ... ok
test_getter_returns_stored_value (test_temperature.CelsiusPropertyTests.test_getter_returns_stored_value)
The constructor value is readable through the getter. ... ok
test_setter_updates_value (test_temperature.CelsiusPropertyTests.test_setter_updates_value)
Assigning through the property replaces the value. ... ok
test_below_absolute_zero_rejected (test_temperature.FahrenheitPropertyTests.test_below_absolute_zero_rejected)
A Fahrenheit value below absolute zero raises. ... ok
test_both_views_stay_in_sync (test_temperature.FahrenheitPropertyTests.test_both_views_stay_in_sync)
Changing Celsius immediately changes Fahrenheit. ... ok
test_fahrenheit_is_derived_from_celsius (test_temperature.FahrenheitPropertyTests.test_fahrenheit_is_derived_from_celsius)
The getter applies the standard conversion formula. ... ok
test_setter_converts_back_to_celsius (test_temperature.FahrenheitPropertyTests.test_setter_converts_back_to_celsius)
Storing Fahrenheit updates the Celsius value. ... ok

----------------------------------------------------------------------
Ran 36 tests in 0.001s

OK
```

Стиль кода — `uv run --with flake8 flake8 lab3 tests`
(max-line-length = 79 из `setup.cfg`); вывод пуст, код чистый:

```text
```

История коммитов — `git log --oneline`
(снимок на 2026-10-01, до merge ветки и тега):

```text
f99d7dc feat: add package exports and demo entry point
152e348 feat: add temperature property task
be8b12f feat: add singleton pattern task
2a21618 feat: add countdown iterator task
468b1ca feat: add counter class task
8106c35 feat: add figure class task
b2ece5b docs: create initial project skeleton
```

CI: GitHub Actions workflow `.github/workflows/python-checks.yml`
с matrix-стратегией по версиям Python `["3.12", "3.13"]`.
