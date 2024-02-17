""""
Функція caching_fibonacci() повинна повертати внутрішню функцію fibonacci(n).
fibonacci(n) обчислює n-те число Фібоначчі. Якщо число вже знаходиться у кеші, функція має повертати значення з кешу.
Якщо число не знаходиться у кеші, функція має обчислити його, зберегти у кеш та повернути результат.
Використання рекурсії для обчислення чисел Фібоначчі.
"""

def caching_fibonacci():
    cache = dict()

    def fibonacci(n):
        if n <= 0: return 0
        if n == 1: return 1
        if n in cache: return cache[n]
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    return fibonacci
fib = caching_fibonacci()
print(fib(10))
print(fib(15))
