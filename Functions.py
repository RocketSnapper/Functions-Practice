def add_numbers(number_one, number_two):
    sum = number_one + number_two
    return sum

number_sum = add_numbers(5, 8)
print(number_sum)

def combine_names(name_one, name_two):
    new_name = name_one + name_two
    return new_name

mixed_name = combine_names('Jim', 'Bob')
print(mixed_name)

def individual_characters(car):
    for characters in car:
        print(characters)

individual_characters('Genesis')

def count_characters(sport):
    if len(sport) >= 3:
        print(sport)
    else:
        print('We need a larger string to print')

count_characters('Hockey')