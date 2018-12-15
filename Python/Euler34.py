def digit_factorials():

    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)

    def curious_number(n):
        digits = list(str(n))
        total = 0
        for digit in digits:
            total += factorial(int(digit))
        if total == n:
            return True
        else: 
            return False
    
    sum_of_curious_numbers = 0
    for i in range(3,1000000):
        if curious_number(i) == True:
            sum_of_curious_numbers += i
    return sum_of_curious_numbers

print(digit_factorials())
    