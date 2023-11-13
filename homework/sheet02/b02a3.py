# Philip Laskowicz

# Please do not name your variables like this. Use camelCase or snake_case instead of PascalCase.
# Also, dont use single letter variables. Use descriptive names instead.
# Had to be done like this due to the exercise.
w = input("Please enter a string of characters: ")

# === Task a ===
# Count the number of vowels in w.
vowels = ["A", "E", "I", "O", "U"]
vowel_count = dict()
for vowel in vowels:
    vowel_count[vowel] = w.upper().count(vowel)

vowel_count["Gesamt"] = sum(vowel_count.values())

# Please do not use print statements like this. Use f-strings with a descriptive output instead.
for vowel, count in vowel_count.items():
    print(f"{vowel}: {count}")


# === Task b ===
# Split w into two substrings of equal length and reverse them.
first_half = w[:len(w) // 2]
second_half = w[len(w) // 2:]
second_first_w = second_half + first_half

# Again, dont do this.
print(second_first_w)


# === Task c ===
# Get unicode values of all characters in w and calculate the sum.
unicode_nums = []
for char in w:
    unicode_nums.append(ord(char))

sum_unicode_nums = sum(unicode_nums)
is_sum_10_div = sum_unicode_nums % 10 == 0

# And once more, dont do this.
print(" ".join(map(str, unicode_nums)))
print(sum_unicode_nums, is_sum_10_div)