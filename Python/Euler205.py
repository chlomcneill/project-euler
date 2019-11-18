import itertools


def peter_possible_outcomes():
    dice = [1, 2, 3, 4]
    possible_outcomes = list(itertools.product(dice, repeat=9))
    # print(possible_outcomes)
    possible_outcomes = [sum(outcome) for outcome in possible_outcomes]
    # print(possible_outcomes)
    return possible_outcomes


def colin_possible_outcomes():
    dice = [1, 2, 3, 4, 5, 6]
    possible_outcomes = list(itertools.product(dice, repeat=6))
    # print(possible_outcomes)
    possible_outcomes = [sum(outcome) for outcome in possible_outcomes]
    # print(possible_outcomes)
    return possible_outcomes


def find_probability():
    peter_outcomes = peter_possible_outcomes()
    colin_outcomes = colin_possible_outcomes()

    possible_score_combinations = len(peter_outcomes) * len(colin_outcomes)
    count = 0

    for p_outcome in peter_outcomes:
        for c_outcome in colin_outcomes:
            if p_outcome > c_outcome:
                count += 1

    return count / possible_score_combinations


print(find_probability())
# Answer = 0.5731440767829801

