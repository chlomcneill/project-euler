# def fib(n):
#    if n == 1:
#       return 1
#    elif n == 0:   
#       return 0            
#    else:                      
#       return fib(n-1) + fib(n-2) 

# Python 3 Program to find 
# sum of Fibonacci numbers 
  
  
# Computes value of first 
# fibonacci numbers 
# def calculateSum(n) : 
#     fibo = [0] * (n)
#     fibo[0] = 1
#     fibo[1] = 2
#     # Initialize result 
#     sm = fibo[0] + fibo[1] 
   
#     # Add remaining terms 
#     for i in range(2,n) : 
#         fibo[i] = fibo[i-1] + fibo[i-2] 
#         sm = sm + fibo[i] 
          
#     return sm 
  
  
# # Driver program to test 
# # above function 
# print("Sum of Fibonacci numbers is: ", calculateSum(4))

a, b = 1, 2
total = 0
while a <= 4000000:
    if a % 2 == 0:
        total += a
    a, b = b, a+b  # the real formula for Fibonacci sequence
print total


