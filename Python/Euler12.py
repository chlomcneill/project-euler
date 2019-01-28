import math

# def first_n_triangle_numbers(n):
#     triangle_nums = [1]
#     for i in range(2,n+1):
#         triangle_nums.append(triangle_nums[-1]+i)
#     return triangle_nums

def nth_triangle_number(n):
    return int(n*(n+1)/2)

def number_of_divisors(n):
    divisors = [1,n]
    for i in range(2,int((n/2)+1)):
        if n % i == 0:
            divisors.append(i)
    return len(divisors)

def first_triangle_num_with_more_than_n_divisors(n):
    for i in range(10000):
        if number_of_divisors(nth_triangle_number(i)) > n:
            print(nth_triangle_number(i))
            break


print(first_triangle_num_with_more_than_n_divisors(500))