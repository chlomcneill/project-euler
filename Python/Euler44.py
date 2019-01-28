import itertools

pentagonal_numbers = []
for num in range(1,1000):
    pentagon_num = (num*((3*num)-1))/2
    pentagonal_numbers.append(pentagon_num)

# print(pentagonal_numbers)

pairs_diff = []
for x, y in itertools.combinations(pentagonal_numbers, 2):
    if abs(x-y) in pentagonal_numbers:
        pairs_diff.append([x,y])

pairs_sum = []
for x, y in itertools.combinations(pentagonal_numbers, 2):
    if (x+y) in pentagonal_numbers:
        pairs_sum.append([x,y])

def diff(elem):
    return abs(elem[0]-elem[1])

pairs_diff.sort(key=diff)

print(pairs_diff[:5])
print(pairs_sum[:5])

# print(pairs_diff[0])

# print(pairs_sum)

# def common_elements(list1, list2):
#     return list(set(list1) & set(list2))

# pairs_diff_and_sum = common_elements(pairs_diff, pairs_sum)
# for pair in pairs_diff:
#     if pair in pairs_sum:
#         pairs_diff_and_sum.append(pair)


# for pair in pairs_diff:
#     if pair in pairs_sum:
#         print(pair)
#         break

# print(pairs_diff_and_sum)




