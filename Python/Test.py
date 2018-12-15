# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

# print factorial(0)
# print factorial(3)

######################################

# def listOfStr_to_listOfInt(n):
#     n = [int(i) for i in n]
#     return n

# x = ['1','2','3','4','5','-6']
# print listOfStr_to_listOfInt(x)

######################################

# def split_list(a_list):
#     half = len(a_list)//2
#     return [a_list[:half], a_list[half:]]

# A = [1,2,3,4,5,6]
# print split_list(A)

######################################

# A utility function to calculate area of the triangle formed by (x1, y1), (x2, y2) and (x3, y3) 
  
def area(x1, y1, x2, y2, x3, y3): 
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)

# A function to check whether point P(x, y) lies inside the triangle formed by A(x1, y1), B(x2, y2) and C(x3, y3)  
def isInside(x1, y1, x2, y2, x3, y3, x, y): 
    A = area (x1, y1, x2, y2, x3, y3) # Calculate area of triangle ABC   
    A1 = area (x, y, x2, y2, x3, y3) # Calculate area of triangle PBC
    A2 = area (x1, y1, x, y, x3, y3) # Calculate area of triangle PAC   
    A3 = area (x1, y1, x2, y2, x, y) # Calculate area of triangle PAB
    # Check if sum of A1, A2 and A3 is same as A 
    if(A == A1 + A2 + A3): 
        return True #P(x ,y) lies inside the triangle
    else: 
        return False #P(x ,y) doesn't lie inside the triangle

######################################