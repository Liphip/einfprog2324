# Philip Laskowicz

x = int(input("x: "))


# Claculate the closest multiple of 100 to x.
closest_multiple = abs(x) // 100 * 100

# Add 100 if the remainder is greater or equal to 50.
if abs(x) % 100 >= 50:
    closest_multiple += 100

# Add the sign of x.
closest_multiple *= x // abs(x)

# Please do not use print statements like this. Use f-strings with a descriptive output instead.
print(closest_multiple)