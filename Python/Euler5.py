from fractions import gcd
  
def number_divisible_by_nums_from_1_to_n(n): 
    ans = 1    
    for i in range(1, n + 1): 
        ans = (ans * i)/gcd(ans, i)         
    return ans 

print(number_divisible_by_nums_from_1_to_n(20))
