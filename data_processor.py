# data_processor.py
# Модуль для обработки списков чисел с разными операциями.

import time
from typing import List, Union

def slow_fibonacci(n: int) -> int:
    """Рекурсивное вычисление Фибоначчи (очень медленно)."""
    if n <= 1:
        return n
    return slow_fibonacci(n-1) + slow_fibonacci(n-2)

def process_numbers(data: List[Union[int, float]]) -> dict:
    """Вычисляет сумму, среднее, максимум и минимум."""
    total = 0
    for x in data:
        total += x
    avg = total / len(data)
    max_val = max(data)
    min_val = min(data)
    return {"sum": total, "avg": avg, "max": max_val, "min": min_val}

def find_duplicates(items: list) -> list:
    """Находит дубликаты в списке (неэффективно)."""
    duplicates = []
    for i in range(len(items)):
        for j in range(i+1, len(items)):
            if items[i] == items[j] and items[i] not in duplicates:
                duplicates.append(items[i])
    return duplicates

def slow_sort(data: list) -> list:
    """Пузырьковая сортировка (O(n^2))."""
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data

def cache_decorator(func):
    """Простой декоратор для кэширования результатов (без очистки)."""
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

@cache_decorator
def expensive_computation(x: int, y: int) -> int:
    """Имитация дорогой операции (засыпает на 1 сек)."""
    time.sleep(1)
    return x * y + x + y

def main():
    data = [4, 2, 7, 2, 9, 1, 9, 3]
    print("Processed:", process_numbers(data))
    print("Duplicates:", find_duplicates(data))
    print("Sorted:", slow_sort(data.copy()))
    print("Fibonacci(30):", slow_fibonacci(30))
    print("Expensive result:", expensive_computation(3, 7))

if __name__ == "__main__":
    main()
