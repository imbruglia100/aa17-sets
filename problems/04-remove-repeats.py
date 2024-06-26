# Given two strings, write a function, `remove_repeats` that returns a set of
# the uncommon characters from both strings. Do NOT use the `^` operator.

# Write your code here.
def greater_than_one(pair):
    return pair[1] <= 1

def remove_repeats(str1, str2):
    char_dict = {x: 1 for x in str1}
    delete_set = set()

    for char in str2:
        if not char_dict.get(char):
            char_dict[char] = 1
        else:
            delete_set.add(char)

    for char in delete_set:
        del char_dict[char]

    return set(char_dict.keys())


str1 = 'aloha'
str2 = 'bonjour'

print(remove_repeats(str1, str2))    # {'r', 'a', 'l', 'h', 'n', 'b', 'j', 'u'}

# def my_filtering_function(pair):
#   pass

# grades = {'John': 7.8, 'Mary': 9.0, 'Matt': 8.6, 'Michael': 9.5}
#
# filtered_grades = dict(filter(my_filtering_function, grades.items()))
