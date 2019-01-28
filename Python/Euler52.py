def list_digits(x):
    return list(str(x))

def same_digit_check(x):
    digits = list_digits(x)
    if list_digits(2*x) == digits and list_digits(3*x) == digits and list_digits(4*x) == digits and list_digits(5*x) == digits and list_digits(6*x) == digits:
        return True
    else:
        return False

i = 0
while i == 0:
    for n in range(100000):
        if same_digit_check(n):
            i = n

print(i) 
