# Operators - An operator is a symbol that performs an operation on variables or values.
a= 10
b = 5
print(a+b)
# Output 
# 15
# Here + is the operator.
#------------------------------------------------------------
# 2. Arthimetic Operators
""" Used for mathematical Calculations. 
Operator -->Meaning --> Example
+ --> Addition --> 10 + 5
- --> Subtraction --> 10 - 5
* --> Multiplication --> 10 * 5
/ --> Division --> 10 / 5
% --> Modulus --> 10 % 3
// --> Floor Division --> 10 // 3
** --> Power --> 2**3
"""
# Example 1: Basic Arthimetic
num1 = 20
num2 = 5

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)

# Output
# Addition: 25
# Subtraction: 15
# Multiplication: 100
# Division: 4.0
#--------------------------------------------------------
# Example 2: Modulus
number = 10
print(number % 3)
# Output
# 1
#------------------------------------------------------
# Example 3: Even/Odd Check
number = 8

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# Output
# Even Number
#-------------------------------------------
# Assignment Operators
salary = 50000
# Example 
salary = 50000
salary += 5000  # salary = salary + 5000
print(salary)
# Output
# 55000



