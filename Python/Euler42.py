import string


f = open('/Users/mcneillc/Documents/project-euler/Python/Text Files/Euler42.txt', "r")
words = f.readlines()[0].split('","')
f.close()


def triangle_number(n):
    return int(0.5 * n * (n+1))


def list_of_triangle_numbers(n):
    tri_nums = []
    for i in range(n+1):
        tri_nums.append(triangle_number(i))
    tri_nums.pop(tri_nums[0])
    return tri_nums


def letter_value(letter):
    letters = list(string.ascii_uppercase)
    if letter in letters:
        return letters.index(letter) + 1
    else:
        return 0


def word_value(word):
    count = 0
    for letter in word:
        count += letter_value(letter)
    return count


def triangle_words():
    tri_nums = list_of_triangle_numbers(50)
    tri_words = []
    for word in words:
        if word_value(word) in tri_nums:
            tri_words.append(word)
    return len(tri_words)



# print(list_of_triangle_numbers(50))

# print(letter_value('B'))
#
# print(word_value('SKY'))

# print(words)

print(triangle_words())