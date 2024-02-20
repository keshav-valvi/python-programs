# KESHAV VALVI
# FY23N052

# Program to print GCD of two numbers without using recursion
import math

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
result = math.gcd(a, b)
print("The GCD of", a, "and", b, "is:", result)

# Program to print the GCD of two numbers using recursion
def hcf(x, y):
    if y == 0:
        return x
    else:
        return hcf(y, x % y)

print("\n\nThe GCD of", a, "and", b, "using recursion:", end=" ")
print(hcf(a, b))