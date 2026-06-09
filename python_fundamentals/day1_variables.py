# Variables - A variable is a name used to store data in memory.
"""
Rules for variables:
1.Must start with a letter or underscore _
2.Cannot start with number
3.Case-sensitive (name ≠ Name)
4.No special characters like @,$,%

Types of variables (Data Types)
1.String - "Hello" 
2.Integer - 10 
3.Float - 10.5 
4.Boolean - True/False

String - Used to store text data
Integer - Used to store whole numbers.
Float -  Used for decimal values.
Boolean - Stores True or False values.
----------------------------------------
Multiple Variables - You can store multiple values separately.
Variable Concatenation - Combine strings using +.
Type Checking - Check variable type using type().
8. Simple Arthimetic - Variables can store calculation results.
9. Real-world Example (Salary Calculation) - Variables simulate real business logic.
10. Swap Variables - Swap values without extra variable.
""" 
#----------------------------------------------------------------------------
#1.String
name = "Shavez"  # Here: name → variable and "Shavez" → value stored in it
print(name)
# Output: Shavez
#--------------------------------------------------------------------
#2.Integer Variable
age = 25
print(age)
# Output: 25
#-------------------------------------------------------------------
# 3.Float Variable
salary = 55000.75
print(salary)
# Output = 55000.75 
#--------------------------------------------------------------------
# 4.Boolean Variable
is_employee = True
print(is_employee)
# Output - True
#---------------------------------------------------------------------
# Multiple Variables
name = "Shavez"
age = 25
city = "Pune"

print(name)
print(age)
print(city)
#Output:
# Shavez
# 25 
# Pune 
#-----------------------------------------------------------------
# Variable Concatenation
first_name = "Shaik"
last_name = "Shavez"

full_name = first_name + " " + last_name
print(full_name)
# Output
# Shaik Shavez
#-----------------------------------------------------------------
#Type Checking
name = "Shavez"
age = 25

print(type(name))
print(type(age))
#Output
#<class 'str'>
#<class 'int'>
#------------------------------------------------------------------
# Simple Arthimetic
a = 10
b = 5
result = a + b
print(result)
# Output
# 15
#-------------------------------------------------------------
# Real world example (Salary Calculation)
basic_salary = 40000
bonus = 5000.66

total_salary = basic_salary + bonus

print("Total Salary:", total_salary)
# Output
# Total Salary: 45000.66
#----------------------------------------------------------------
#Swap Variables
a = 10
b = 20
a,b = b,a
print("a = ", a)
print("b = ", b)
# Output
# a = 20
# b = 10

""" Practice Tasks
 1. Employee Details - Store employee information.
2. Calculator Basics - Perform arithmetic operations.
3. Product Calculation - Used in e-commerce/testing logic.
4. System Message Format - Used in logs/testing output validation.
5. Debug Practice - Find variable values using print.
"""
#-------------------------------------------------------------------------
# 1. Employee Details
Employee_name = "Shaik Shavez"
Employee_ID = 12345
Department = "QA"
print(Employee_name, Employee_ID, Department)
# Output - Shavez, 12345, QA
#-----------------------------------------------------------------------
# 2. Calculator Basics
a = 15
b = 5
print("Add:", a + b)
print("Sub:", a - b)
print("Mul:" ,a * b)
print("Div:", a / b)

# Output 
# Add: 20
# Sub: 10
# Mul: 75
# Div: 3.0
#-------------------------------------------------------------------
# 3. Product Calculation.
product = "Mouse"
price = 500
quantity = 2

total = price * quantity

print(product)
print("Total Price:", total)
# Output 
# Mouse
# Total Price: 1000
#----------------------------------------------------------
# 4.System Message Format
user = "Admin"
status = "Logged In"

print(user + " has " + status)
# Output
# Admin has Logged In
#--------------------------------------------------
# 5.Debug Practice
x = 100
y = 200
z = x + y

print("x =", x)
print("y =", y)
print("z =", z)
# Output
# x = 100
# y = 200
# z = 300
#---------------------------------------------------------

















 



