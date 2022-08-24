def fibonacci_generator():
    a, b = 0, 1
    yield a
    while True:
        yield b
        a, b = b, a+b
