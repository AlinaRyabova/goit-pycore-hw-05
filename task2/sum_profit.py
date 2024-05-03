from typing import Callable

def sum_profit(text: str, func: Callable):
    # Використовуємо функцію-генератор для отримання чисел
    numbers_generator = func(text)
    # Сумуємо всі числа
    total = sum(numbers_generator)
    return total