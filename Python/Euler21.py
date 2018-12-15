def amicable_nums(limit):
    
    def sum_of_divisors(n):
        list_of_divisors = []
        for num in range(1, n):
            if n % num == 0 and num not in list_of_divisors:
                list_of_divisors.append(num)
        return sum(list_of_divisors) 

    list_of_amicable_nums = []
    for a in range(1,limit):
        for b in range(1,limit):
            if sum_of_divisors(a) == b and sum_of_divisors(b) == a and a!=b and (a,b) not in list_of_amicable_nums:
                list_of_amicable_nums.append(a,b)
    return sum(list_of_amicable_nums)

print amicable_nums(10000)

    


