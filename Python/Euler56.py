def power_up(a,b):
    return a ** b

def digital_sum(n):
    digit_sum = sum(int(digit) for digit in str(n))
    return digit_sum

maximum_digital_sum = 0

for a in range(100):
    for b in range(100):
        if digital_sum(power_up(a,b)) > maximum_digital_sum:
            maximum_digital_sum = digital_sum(power_up(a,b))

print(maximum_digital_sum)

