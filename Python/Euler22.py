import string

f = open('/Users/mcneillc/Documents/project-euler/Python/Text Files/Euler22.txt', "r")
names = f.readlines()[0].split(',')
names = [name[1:-1] for name in names]
names = sorted(names)
f.close()


def letter_value(letter):
    alphabet = list(string.ascii_uppercase)
    if letter in alphabet:
        return alphabet.index(letter) + 1
    else:
        return 0


def name_value(name):
    score = 0
    for letter in name:
        score += letter_value(letter)
    return score


def name_scores():
    total_score = 0
    for name in names:
        total_score += name_value(name) * (names.index(name) + 1)
    return total_score


print(name_scores())






