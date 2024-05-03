def caching_fibonacci():
    # Створюємо порожній словник для зберігання обчислених значень чисел Фібоначчі
    cache = {}

    def fibonacci(n):
        # Якщо n менше або рівне 0, повертаємо 0
        if n <= 0:
            return 0
        # Якщо n дорівнює 1, повертаємо 1
        elif n == 1:
            return 1
        # Якщо n вже є у кеші, повертаємо відповідне значення
        elif n in cache:
            return cache[n]
        # Якщо n  не знаходиться у кеші, обчислюємо його рекурсивно
        else:
            # Обчислюємо n число Фібоначі та зберігаємо його у кеші
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cache[n]

    # Повертаємо внутрішню функцію fibonacci
    return fibonacci

fib = caching_fibonacci()
print(fib(7))
print(fib(25))
print(fib(35))     