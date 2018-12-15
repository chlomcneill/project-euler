import math 
  
def prime_factors_of_n(n): 
    while n % 2 == 0: 
        print(2) 
        n = n / 2
    for i in range(3, int(math.sqrt(n))+1, 2): 
        while n % i == 0: 
            print(i) 
            n = n / i 
    if n > 2: 
        print(n) 
  
prime_factors_of_n(600851475143)  