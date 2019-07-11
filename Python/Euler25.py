def next_fibonacci_number(prev1, prev2):
    return prev1 + prev2


def digits_in_n(n):
    return len(str(n))


def fibonacci_sequence():
    f1 = 1
    f2 = 1
    fib = [f1, f2]
    next_fib = next_fibonacci_number(fib[-1], fib[-2])
    while digits_in_n(next_fib) < 1000:
        fib.append(next_fib)
        next_fib = next_fibonacci_number(fib[-1], fib[-2])
    return fib.index(fib[-1])+2


print(fibonacci_sequence())
# print(digits_in_n(12340000000))