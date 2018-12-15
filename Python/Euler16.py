def power_digit_sum(number, power):
    n = number ** power
    digits = [int(d) for d in str(n)]
    digit_sum = 0
    for i in digits:
        digit_sum += i
    return digit_sum

print power_digit_sum(2,1000)
