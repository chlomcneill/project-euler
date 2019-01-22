def power_digit_sum(number, power):
    n = number ** power
    digit_sum = sum([int(d) for d in str(n)])
    return digit_sum

print(power_digit_sum(2,1000))
