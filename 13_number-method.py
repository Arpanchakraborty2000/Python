import math

# Example number
num = -25.75

print("Original number:", num)

# Built-in number methods/functions
print("Absolute value (abs):", abs(num))
print("Round number (round):", round(num))
print("Round with 2 decimals:", round(num, 2))
print("Power (pow):", pow(2, 3))  # 2^3
print("Maximum (max):", max(10, 20, 30))
print("Minimum (min):", min(10, 20, 30))
print("Convert to int:", int(25.99))
print("Convert to float:", float(10))
print("Convert to complex:", complex(3, 4))

# Math module functions
x = 16
print("\nMath module examples")
print("Square root:", math.sqrt(x)) # not use nagative funtion 
print("Ceiling (ceil):", math.ceil(25.1))
print("Floor:", math.floor(25.9))
print("Factorial:", math.factorial(5))
print("Greatest Common Divisor (gcd):", math.gcd(48, 180))
print("Log base e:", math.log(10))
print("Log base 10:", math.log10(100))
print("Pi value:", math.pi)
print("e value:", math.e)

print("math.fabs(-10) =", math.fabs(-10))
print("math.fabs(-25.75) =", math.fabs(-25.75))
print("math.fabs(100) =", math.fabs(100))



print("math.exp(1) =", math.exp(1))     # e^1
print("math.exp(2) =", math.exp(2))     # e^2
print("math.exp(0) =", math.exp(0))     # e^0
print("math.exp(-1) =", math.exp(-1))   # e^-1


# Trigonometric functions
angle = math.radians(90)  # Convert degree → radian
print("\nTrigonometry")
print("sin(90°):", math.sin(angle))
print("cos(90°):", math.cos(angle))
print("tan(45°):", math.tan(math.radians(45)))

# Checking number properties
print("\nCheck properties")
print("Is 25.75 finite? ", math.isfinite(num))
print("Is NaN? ", math.isnan(5))   # False
print("Is infinite? ", math.isinf(5))  # False
