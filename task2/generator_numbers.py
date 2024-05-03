import re


def generator_numbers(text: str):
    # Регулярний вираз для пошуку дійсних чисел, розділених пробілами
    pattern = r'\b\d+\.\d+\b'
    # Знаходимо всі числа у тексті та повертаємо генератор
    for match in re.finditer(pattern, text):
        yield float(match.group())



