import os
def call_counter(path):
    def decorator(func):
        count = 0

        def wrapper(*args, **kwargs):
            nonlocal count
            count += 1
            with open(path, 'a') as f:
                f.write(f"Function '{func.__name__}' was called {count} times\n")
            return func(*args, **kwargs)

        return wrapper

    return decorator

@call_counter('data.txt')
def add(a, b):
    return a + b

print(add(4, 6))
print(add(3, 5))