# Philip Laskowicz

input_str = input("Please enter a number: ")

input_nums = []

while input_str != "":
    input_nums.append(int(input_str))
    input_str = input("Please enter a number or nothing to exit: ")

input_nums.sort()
sum_nums = sum(input_nums)
average = sum_nums / len(input_nums)
min_num = input_nums[0]
max_num = input_nums[-1]

# Please do not use print statements like this. Use f-strings with a descriptive output instead.
print(sum_nums, average, min_num, max_num)