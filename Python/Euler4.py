# Program to check if a string
#  is palindrome or not

# change this value for a different output
# my_str = '90809'

# # make it suitable for caseless comparison
# my_str = my_str.lower()

# # reverse the string
# rev_str = reversed(my_str)

# # check if the string is equal to its reverse
# if list(my_str) == list(rev_str):
#    print("It is palindrome")
# else:
#    print("It is not palindrome")



# a = []
# for i in range(100,1000):
#     if list(str(i)) == list(reversed(str(i))):
#         a.append(i)

b = []
for j in range(100,1000):
    for k in range(100,1000):
        if list(str(j*k)) == list(reversed(str(j*k))):
            b.append((j,k))

c=[0]
for (j,k) in b:
    if j*k > c[0]:
        c[0]=j*k
print c[0]       