# the tuple is the collection of homogenous or heterogenous data.
# enclosed between Parenthesis ().

"""syntax: 
        var_name = (val1, val2, val3, ..., valn)
                        or
        var_name = val1, val2, val3, ..., valn
                        or
        var_name = (val1) # to initialize single element in tuple.

"""


# Eg 1.
numbers = (1, 3, 4, 5)
# print(numbers)

first=numbers[1]
# print(first)

# checking type of numbers 
# print(type(numbers))

mix_tuple = ("Akshay", "Surase", "Kajal", "Rajgurav", 12, 1.22, True)
# print(mix_tuple)

getSecond = mix_tuple[1]
print(getSecond)


get_length = len(getSecond)
get_length_tuple = len(mix_tuple)

print(get_length)
print(get_length_tuple)



