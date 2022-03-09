a = ")("


def remove_one_part(start_string):
    possible_answers = []
    for i in range(len(start_string)):

        # Skip the removal of "a" chars
        if start_string[i] not in ["(", ")"]:
            continue

        poss_ans = start_string[:i] + start_string[i + 1:]
        possible_answers.append(poss_ans)
    return possible_answers


def is_valid(input_string):
    unclosed_para = 0
    for letter in input_string:
        if letter == "(":
            unclosed_para += 1
        elif letter == ")":
            unclosed_para -= 1

        if unclosed_para < 0:
            return False

    return unclosed_para == 0


# Max number of chars to try and remove
max_removals = len(a)
current_possible = [a]
for remove in range(max_removals):
    new_possible = set()

    for poss in current_possible:
        new_removed_poss = remove_one_part(poss)
        for poss in new_removed_poss:
            new_possible.add(poss)

    is_valid_bool_list = list(map(is_valid, new_possible))
    if any(is_valid_bool_list):
        print(f"Finished Early at {remove} iterations")

        # Create final list of shortest valid strings
        final_list = []
        new_possible = list(new_possible)
        for i, is_valid_bool in enumerate(is_valid_bool_list):
            if is_valid_bool:
                final_list.append(new_possible[i])

        # Print and stop after possibilities have been calculated
        print(set(final_list))
        break

    current_possible = new_possible