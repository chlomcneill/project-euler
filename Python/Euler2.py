def sum_of_even_valued_fib_nums_below_n(n):
    a, b = 1, 2
    total = 0
    while a <= n:
        if a % 2 == 0:
            total += a
        a, b = b, a+b  # the real formula for Fibonacci sequence
    return total

print(sum_of_even_valued_fib_nums_below_n(4000000))