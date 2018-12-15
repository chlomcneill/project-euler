# def listsum(numList):
#     theSum = 0
#     for j in numList:
#         if j%3==0 or j%5==0:
#             theSum = theSum + j
#     return theSum

# print(listsum(range(1,1000)))

def func(n):
    total = 0
    for i in range(1,n):
        if i%3==0 or i%5==0:
            total+=i
    print total

func(10)