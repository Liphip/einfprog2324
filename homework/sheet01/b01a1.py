# Philip Laskowicz

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
d = int(input("d: "))
x = int(input("x: "))


# Calculate the polynomial a*x^3 + b*x^2 + c*x + d.
poly = a*x**3 + b*x**2 + c*x + d

# Please do not use print statements like this. Use f-strings with a descriptive output instead.
print(poly)