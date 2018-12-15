def distinct_powers(a,b):
    a_range = range(2,a+1)
    b_range = range(2,b+1)
    list_of_distinct_powers = []
    for x in a_range:
        for y in b_range:
            if x ** y not in list_of_distinct_powers:
                list_of_distinct_powers.append(x**y)
    return len(list_of_distinct_powers)

print(distinct_powers(100,100))
