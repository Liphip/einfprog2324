# Read numbers until the user enters nothing.
input_str = input("Please enter a number: ")

input_nums = []

while input_str != "":
    input_str_num = int(input_str)
    input_nums.append(input_str_num) if 0 < input_str_num <= 127 else None
    input_str = input("Please enter a number or nothing to exit: ")

# Convert numbers to ascii characters and join them to a string.
ascii_str = "".join(map(chr, input_nums))

# Please do not use print statements like this. Use f-strings with a descriptive output instead.
print(ascii_str)