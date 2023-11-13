# Philip Laskowicz

input_num = int(input("Please enter a number: "))

# === Task a ===
# Calculate cross sum of input_num.
cross_sum = 0
input_num_copy = abs(input_num)
while input_num_copy > 0:
    cross_sum += input_num_copy % 10
    input_num_copy //= 10

# Please do not use print statements like this. Use f-strings with a descriptive output instead.
print(cross_sum)


# === Task b ===
# Calculate the number of real divisors of input_num.
real_divisors = 0
for i in range(1, abs(input_num) + 1):
    if input_num % i == 0:
        real_divisors += 1

# Again, dont do this.
print(real_divisors)