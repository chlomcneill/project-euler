def sum_of_multiples_of_3_and_5_below_n(n):
    total = 0
    for i in range(1,n):
        if i%3==0 or i%5==0:
            total+=i
    return total

print(sum_of_multiples_of_3_and_5_below_n(10))