def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def factorial_digit_sum(n): 
    digits = [int(d) for d in str(factorial(n))]
    digit_sum = 0
    for i in digits:
        digit_sum += i
    return digit_sum

print(factorial_digit_sum(100))