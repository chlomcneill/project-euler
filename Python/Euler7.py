def nth_prime_number(n):
    prime_list = [2]
    num = 3
    while len(prime_list) < n+1:
        for p in prime_list:
            if num % p != 0:
                prime_list.append(num)
            num += 2
    return prime_list

print nth_prime_number(6)
