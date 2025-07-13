import time


def growing_symbol_transition(symbol: str = "*", num_lines: int = 7, sleep_seconds: int = 1):
    print(symbol)
    time.sleep(sleep_seconds)
    b = 1
    next = b
    count: int = 1
    while count < num_lines:
        count += 1
        a, b = b, next
        next = a + b
        print(symbol * next)
        time.sleep(sleep_seconds)






