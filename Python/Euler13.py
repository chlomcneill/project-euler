path = '/Users/mcneillc/Documents/Project Euler/Python/Text Files/Euler13.txt'
list_of_numbers = open(path, 'r')

def large_sum():
    numbers = list_of_numbers.readlines()
    count = 0
    for i in numbers:
        count += i 
    return int(str(count)[:10])

print large_sum

