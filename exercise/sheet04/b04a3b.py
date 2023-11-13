# Get ceasar encrypted string.
ceasar_str = input("Please enter a string of characters: ")

# Get the ceasar offset.
ceasar_offset = int(input("Please enter a number: "))

# Convert the string to a list of ascii numbers.
ascii_nums = list(map(ord, ceasar_str))

# Raise an exception if the offset is negative or the highest ascii number is greater than 127 (which is the highest ascii number for a valid character).
ascii_nums_sorted = ascii_nums.copy()
ascii_nums_sorted.sort()
if ceasar_offset < 0 or ascii_nums_sorted[-1] > 127:
    raise Exception("Invalid input!")
del ascii_nums_sorted

# Remove the offset from the ascii numbers with a wrap around.
ceasar_nums = map(lambda num: (num - ceasar_offset) % 128, ascii_nums)

# Convert the ascii numbers back to characters and join them to a string with $ as a separator.
ceasar_str = "$".join(map(chr, ceasar_nums))

# Please do not use print statements like this. Use f-strings with a descriptive output instead.
print(ceasar_str)