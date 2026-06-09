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
# ------------------------------------------------------------
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
# -----------------------------------------------------------------
# Comparision Operators
"""
Comparision Operators compare two values and return True or False

Operator      Meaning
==            Equal
!=            Not Equal
>             Greater than
<             Less than
>=            Greater than or Equal
<=            Less than or Equal
"""
# Example 1
age = 28

print(age == 28)     # Output  - True
print(age > 18)      # Output- True
print(age < 18)      # Output - False

# Example 2 - QA Automation Example
expected_title = "Dashboard"
actual_title = "Dashboard"

print(expected_title == actual_title)  # Output - True
# This is exactly how automated validation works.
# -------------------------------------------------------------
# Logical Operators  - Used to combine multiple conditions.
"""
1. AND Operator - Both conditions must be True.
2. OR Operator - At least one condition must be True.
3. NOT Operator - Reverses the result.
"""
#Example 1  - AND Operator
username = "admin"
password = "1234"

print(username == "admin" and password == "1234") # Output - True
#Example 2 - OR Operator
age = 25

print(age > 18 or age > 60)  # Output - True
#Example 3 - NOT Operator
is_raining = False
print(not is_raining)  # Output - True
#-------------------------------------------------------------
# Conditional Statements - Used to perform different actions based on conditions.
"""
Condition - Conditions help programs make decisions.
# Real Life Example
If username is correct
    Allow login
Else
    Show error
"""
# If Statement - Executes a block of code if a specified condition is true.
# Syntax
"""
if condition:
    statement
"""
# If Statement Example
age = 20
if age >= 18:
    print("Eligible to Vote")   # Output - Eligible to Vote
# ----------------------------------------------------------------------------------------------------------
# If-Else Statement - Executes one block of code if a condition is true, and another block if it is false.
# Syntax
"""
if condition:
    statement
else:
    statement
"""
# If-Else Statement Example
age = 16

if age >= 18:
    print("Adult")
else:
    print("Minor")
# Output - Minor
#-------------------------------------------------------------
# If-Elif-Else Statement - Used to check multiple conditions.
marks = 85
if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
else:
    print("Fail")
# Output - Grade B
#-------------------------------------------------------------
# Automation Oriented Examples
""" 
1. Login Validation - Use if-else to validate user credentials.
2. API Response Validation - Use if-elif-else to check different response codes.
3. Page Title Validation - Use if statement to validate page titles.
4. Firmware Status Validation - Use if-else to check device status.
5. MQTT Message Validation - Use if-elif-else to validate message content.
6. Salary Validation - Use if-else to check if salary meets criteria.
"""
# Example 1 - Login Validation
username = "admin"
password = "1234"
if username == "admin" and password == "1234":
    print("Login Successful")   # Output - Login Successful
else:
    print("Login Failed")   # Output - Login Failed  
# Output - Login Successful
# -------------------------------------------------------------------------
# Example 2 - API Response Validation
response_code = 404
if response_code == 200:
    print("Success")        # Output - Success
elif response_code == 404:
    print("Not Found")      # Output - Not Found                
elif response_code == 500:
    print("Server Error")   # Output - Server Error
else:
    print("Unknown Response")   # Output - Unknown Response
# Output - Not Found
#-----------------------------------------------------------------------------
# Example 3 - Page Title Validation
expected_title = "Dashboard"
actual_title = "Dashboard"                              
if expected_title == actual_title:
    print("Title Validation Passed")   # Output - Title Validation Passed
else:
    print("Title Validation Failed")   # Output - Title Validation Failed
# Output - Title Validation Passed  
#-----------------------------------------------------------------------------
# Example 4 - Firmware Status Validation
device_status = "Online"
if device_status == "Online":
    print("Device is Online")   # Output - Device is Online
else:
    print("Device is Offline")  # Output - Device is Offline
# Output - Device is Online
#-----------------------------------------------------------------------------
# Example 5 - MQTT Message Validation
message = "Temperature: 25°C"

if "Temperature" in message:
    print("Temperature Data Received")   # Output - Temperature Data Received
else:

    print("Unknown Message")   # Output - Unknown Message
# Output - Temperature Data Received
#-----------------------------------------------------------------------------
# Example 6 - Salary Validation
salary = 60000
if salary >= 50000:
    print("Salary meets criteria")   # Output - Salary meets criteria
else:
    print("Salary does not meet criteria")   # Output - Salary does not meet criteria
# Output - Salary meets criteria
# ------------------------------------------------------------------
# Practice Exercise
# 1. Calculator - Create a simple calculator that performs basic arithmetic operations based on user input.
num1 = 10
num2 = 5
operation = input("Enter operation (+, -, *, /): ")
if operation == "+":
    print("Result:", num1 + num2)
elif operation == "-":
    print("Result:", num1 - num2)
elif operation == "*":
    print("Result:", num1 * num2)
elif operation == "/":
    print("Result:", num1 / num2)
else:
    print("Invalid Operation")
# Output - Depends on user input
# -----------------------------------------------------------------
# 2.Even or Odd Checker - Write a program that checks if a number is even or odd.
number = int(input("Enter a number: ")) 
if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")
# Output - Depends on user input
# -----------------------------------------------------------------
# 3. Grade Calculator - Create a program that assigns grades based on marks.
marks = int(input("Enter marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")

elif marks >= 70:
    print("Grade C")
else:
    print("Fail")   
# Output - Depends on user input
# -----------------------------------------------------------------
# 4. Login System - Implement a simple login system that validates username and password.
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Login Failed")

# Output - Depends on user input
# -----------------------------------------------------------------
# 5. API Response Checker - Write a program that checks API response codes and prints appropriate messages.
response_code = int(input("Enter API response code: ")) 
if response_code == 200:
    print("Success")
elif response_code == 404:
    print("Not Found")
elif response_code == 500:
    print("Server Error")
else:
    print("Unknown Response")
# Output - Depends on user input
# -----------------------------------------------------------------


















