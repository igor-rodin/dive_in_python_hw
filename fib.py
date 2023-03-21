def fibonacci(n: int) -> int:
    '''
    Генератор первых n чисел Фибоначчи
    '''
    prev, cur = -1, 1
    for _ in range(n):
        fib = prev + cur
        prev, cur = cur, fib
        yield fib


fib = fibonacci(10)
print(*fib)
