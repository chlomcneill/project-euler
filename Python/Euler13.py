f = open('/Users/mcneillc/Documents/project-euler/Python/Text Files/Euler13.txt',"r")
list_of_numbers = f.readlines()
f.close()

def large_sum():
    count = 0
    for i in list_of_numbers:
        count += int(i)
    return str(count)[:10]

print(large_sum())

