# Лабораторная работа №3

Самодуров Матвей Николаевич, группа 221341, вариант 8, лабораторная №3.

## Задания варианта

**Средняя сложность:**

- №4 — класс «Фигура» (площадь, периметр) (`lab3/figure.py`)
- №8 — класс-счётчик (увеличение/уменьшение) (`lab3/counter.py`)
- №10 — класс-итератор обратного отсчёта (`lab3/countdown.py`)

**Повышенная сложность:**

- №1 — паттерн Singleton через метакласс (`lab3/singleton.py`)
- №8 — класс с использованием `property` (`lab3/temperature.py`)

## Клонирование

```bash
git clone https://github.com/kyomufs/mtp-lab3-variant8.git
```

## Запуск

```bash
uv run python -m lab3
```

## Проверки

```bash
uv run python -m unittest discover -s tests -v
uv run --with flake8 flake8 lab3 tests
```

Подробное описание выполнения — в `docs/report.md`.
