fibonacci_cache = {}
def fibonacci(n):
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n>2:
        value = fibonacci(n-1) + fibonaacci(n-2)
        fibanacci_cache[n] = value
        return value
    
    for n in range(1,1001):
        print(n,' : ', fibonacci(n))

fibonacci(2)
