def self_powers(n):
    return n ** n

def sum_of_self_powers(n):
    total = 0
    for i in range(1,n+1):
        total += self_powers(i)
    return total

print sum_of_self_powers(1000)