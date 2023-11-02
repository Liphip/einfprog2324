# Philip Laskowicz

# Please do not name your variables like this. Use camelCase instead of PascalCase.
# Had to be done like this due to the exercise.
A = int(input("A: "))
B = int(input("B: "))
C = int(input("C: "))


# === Task a ===
# Calculate the integer division of B by A.
div_b_a = B // A

# Please do not use print statements like this. Use f-strings with a descriptive output instead.
print(div_b_a)

# === Task b ===
# Find the median of A, B, and C.
median = None
if B <= A <= C or C <= A <= B:
    median = A
elif A <= B <= C or C <= B <= A:
    median = B
elif A <= C <= B or B <= C <= A:
    median = C

# Again, dont do this.
print(median)

# === Task c ===
# Calculate the absolute difference between A and B. (Without using abs())
abs_diff_a_b = None
if A >= B:
    abs_diff_a_b = A - B
elif B > A:
    abs_diff_a_b = B - A

# And once more, dont do this.
print(abs_diff_a_b)