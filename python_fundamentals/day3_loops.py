"""
This is a very important topic because automation scripts use loops everywhere:

Finding multiple web elements
Reading test data from Excel/CSV
Running test cases repeatedly
Processing API responses
Generating reports

"""
# Loops allow us to execute a block of code multiple times without having to write it out repeatedly.
# This is essential for tasks that require repetition, such as iterating through lists, processing data, or performing actions until a certain condition is met.
# There are two main types of loops in Python:
# 1. For Loop - Used for iterating over a sequence (like a list, tuple, or string).
# 2. While Loop - Repeats as long as a certain boolean condition is met
# For Loop Syntax
"""
for variable in sequence:
    # Code to execute
    # This block will run for each item in the sequence
    # The variable takes the value of each item in the sequence one by one
    """
# Example 1 - Iterating through a list of test cases
# Example 2 - Iterating through a string (like a username)
# While Loop Syntax
"""
while condition:
    # Code to execute
    # This block will run as long as the condition is True
    # Be careful to avoid infinite loops by ensuring the condition eventually becomes False
    """
#-----------------------------------------------------------------------------
# Example 1 - Using a For Loop to iterate through a list of test cases  
test_cases = ["Login Test", "Signup Test", "Checkout Test"]
for test in test_cases:
    print("Running:", test)
# Output:
# Running: Login Test
# Running: Signup Test
# Running: Checkout Test
#-----------------------------------------------------------------------------
# Example 2 - Using a For Loop to iterate through a string (like a username)
username = "Shavez"
for char in username:
    print(char)     
# Output:
# S
# h 
# a
# v
# e
# z
#-----------------------------------------------------------------------------
# Example 3 - Using a While Loop to repeat an action until a condition is met
count = 0
while count < 5:
    print("Count is:", count)
    count += 1  # Increment count to avoid infinite loop
# Output:
# Count is: 0
# Count is: 1   
# Count is: 2
# Count is: 3
# Count is: 4
#-----------------------------------------------------------------------------
# Automation Oriented Examples
"""
1. Web Element Iteration - Use for loops to iterate through lists of web elements. 
2. Test Data Processing - Use for loops to read and process test data from Excel or CSV files.
3. Repeated Test Execution - Use while loops to run test cases repeatedly until a certain condition is met (like a timeout).
4. API Response Handling - Use for loops to iterate through API responses and extract necessary information.
5. Report Generation - Use loops to generate reports based on test results.
"""
# Additional Context - Variables and Operators
"""
Variables are used to store data that can be used and manipulated throughout a program. They are essential for writing dynamic and flexible code.
Operators are symbols that perform operations on variables and values. They are used to perform calculations, comparisons, and logical operations.
Understanding variables and operators is crucial for writing effective loops, as they often involve conditions and calculations that rely on these concepts.
""" 
# Note: The above code snippets for variables and operators are from previous lessons and are included here for context. They are not part of the loops lesson but are essential for understanding how to use loops effectively in automation scripts.
# The loops lesson will build on the concepts of variables and operators to demonstrate how to use them in practical automation scenarios.
# The next step is to implement the automation-oriented examples mentioned above, which will demonstrate how to use loops in real-world testing scenarios.
# For example, we can write a loop to iterate through a list of web elements and perform actions on them, or we can use a while loop to keep trying to log in until we succeed or reach a certain number of attempts.
# -----------------------------------------------------------------------------
# 1. Web Element Iteration - Use for loops to iterate through lists of web elements.
# Example: Simulating a list of web elements (like buttons) and clicking them   
web_elements = ["Button1", "Button2", "Button3"]
for element in web_elements:
    print("Clicking on:", element)
# Output:
# Clicking on: Button1 
# Clicking on: Button2
# Clicking on: Button3
# -----------------------------------------------------------------------------
# 2. Test Data Processing - Use for loops to read and process test data from Excel or CSV files.
# Example: Simulating reading test data from a list (as if it were read from a file)
test_data = ["TestCase1", "TestCase2", "TestCase3"]
for data in test_data:
    print("Processing:", data)
# Output:
# Processing: TestCase1
# Processing: TestCase2
# Processing: TestCase3
# -----------------------------------------------------------------------------
# 3. Repeated Test Execution - Use while loops to run test cases repeatedly until a certain condition is met (like a timeout).
# Example: Simulating a login attempt that keeps trying until it succeeds or reaches a certain number of attempts
attempts = 0
max_attempts = 5
logged_in = False
while not logged_in and attempts < max_attempts:
    print("Attempting to log in... Attempt:", attempts + 1)
    # Simulate a login attempt (for demonstration, we'll just toggle logged_in after 3 attempts)
    if attempts == 2:
        logged_in = True
    attempts += 1       
if logged_in:
    print("Login successful!")
else:    print("Login failed after", max_attempts, "attempts.")
# Output:
# Attempting to log in... Attempt: 1
# Attempting to log in... Attempt: 2    
# Attempting to log in... Attempt: 3
# Login successful!
# -----------------------------------------------------------------------------
# 4. API Response Handling - Use for loops to iterate through API responses and extract necessary information.
# Example: Simulating API responses and extracting status codes     
api_responses = [
    {"status_code": 200, "data": "Success"},
    {"status_code": 404, "data": "Not Found"},
    {"status_code": 500, "data": "Server Error"}
]
for response in api_responses:
    print("Status Code:", response["status_code"], "Data:", response["data"])
# Output:
# Status Code: 200 Data: Success
# Status Code: 404 Data: Not Found
# Status Code: 500 Data: Server Error
# -----------------------------------------------------------------------------
# 5. Report Generation - Use loops to generate reports based on test results.
# Example: Simulating test results and generating a simple report
test_results = [
    {"test_case": "Login Test", "result": "Pass"},
    {"test_case": "Signup Test", "result": "Fail"},
    {"test_case": "Checkout Test", "result": "Pass"}
]   
for result in test_results:
    print("Test Case:", result["test_case"], "Result:", result["result"])       
# Output:
# Test Case: Login Test Result: Pass    
# Test Case: Signup Test Result: Fail
# Test Case: Checkout Test Result: Pass
#-----------------------------------------------------------------------------
# Additional Context - Variables and Operators
"""
1. Variable Naming Rules - Variables must follow specific rules for naming.
2. Data Types - Variables can store different types of data (string, integer, float, boolean).
3. Variable Concatenation - Combine strings using the + operator.
4. Type Checking - Check variable type using the type() function.
5. Simple Arithmetic - Variables can store results of calculations.
6. Real-world Example (Salary Calculation) - Variables can be used to simulate real business logic, like calculating salary after deductions.
7. Swap Variables - You can swap values of two variables without using a temporary variable.
""" 
#------------------------------------------------------------------------------
"""
print("Test Case Executed")
print("Test Case Executed")
print("Test Case Executed")
print("Test Case Executed")
print("Test Case Executed")
"""
# Instead of writing the same print statement multiple times, we can use a loop to execute it repeatedly.
for i in range(5):  # This will run the block of code 5 times

    print("Test Case Executed")  # Output - Test Case Executed (printed 5 times)
#---------------------------------------------------------------------------------
"""
 Syntax:
for variable in sequence:
    code to execute

 """
# Example: Print numbers from 0 to 4 using a for loop
for i in range(5):
    print(i)
# Output:
# 0     
# 1
# 2
# 3
# 4
# --------------------------------------------------------------------------------
# range () - A built-in function that generates a sequence of numbers. It can take one, two, or three arguments:
# range(start, stop, step) - Generates numbers from start to stop (exclusive) with a step value.

#   Example: Print even numbers from 2 to 10 using a for loop and range() function
for i in range(2, 11, 2):
    print(i)
# Output:
# 2             
# 4
# 6
# 8     
# 10
# --------------------------------------------------------------------------------
for i in range(0, 100, 10):
    print(i)
# Output:
# 0
# 10
# 20
# 30
# 40
# 50
# 60
# 70
# 80
# 90
# --------------------------------------------------------------------------------
# Print Odd numbers from 1 to 20
for i in range(1, 20, 2):
    print(i)
# Output:
# 1
# 3
# 5
# 7
# 9
# 11
# 13
# 15
# 17
# 19
# --------------------------------------------------------------------------------
# Loop through list of browsers
browsers = ["Chrome", "Firefox", "Edge"]

for browser in browsers:
    print(browser)
# Output:
# Chrome
# Firefox
# Edge
# --------------------------------------------------------------------------------
# Automation Oriented Example - Iterating through a list of test cases
test_cases = [
    "Login Test",
    "Search Test",
    "Logout Test"
]

for test in test_cases:
    print("Executing:", test)
# Output:
# Executing: Login Test 
# Executing: Search Test
# Executing: Logout Test
# --------------------------------------------------------------------------------
"""
While Loop Syntax:
while condition:
    code to execute
    # This block will run as long as the condition is True
    # Be careful to avoid infinite loops by ensuring the condition eventually becomes False
    """
# Example: Print numbers from 1 to 5 using a while loop
count = 1

while count <= 5:
    print(count)
    count += 1
# Output:
# 1
# 2
# 3
# 4
# 5
# --------------------------------------------------------------------------------
# Infinite Loop Example - Be cautious with while loops to avoid infinite loops
while True:
    print("Running")
    # This will run indefinitely until you stop it manually (e.g., by pressing Ctrl+C)
# Output - Running (printed indefinitely)
# --------------------------------------------------------------------------------
# Automation Oriented Example - Repeated Test Execution
attempts = 0
max_attempts = 3
logged_in = False
while not logged_in and attempts < max_attempts:
    print("Attempting to log in... Attempt:", attempts + 1)
    # Simulate a login attempt (for demonstration, we'll just toggle logged_in after 2 attempts)
    if attempts == 1:
        logged_in = True
    attempts += 1          
if logged_in:
    print("Login successful!")
else:
    print("Login failed after", max_attempts, "attempts.")
# Output:
# Attempting to log in... Attempt: 1    
# Attempting to log in... Attempt: 2
# Login successful!
# --------------------------------------------------------------------------------  
# Break Statement - Used to exit a loop prematurely when a certain condition is met.
# Example: Find the first even number in a list and exit the loop once found
numbers = [1, 3, 5, 6, 7, 8]
for num in numbers:
    if num % 2 == 0:
        print("First even number found:", num)
        break
# Output:
# First even number found: 6
# --------------------------------------------------------------------------------
# Continue Statement - Used to skip the current iteration and move to the next one.
# Example: Print only odd numbers from a list, skipping even numbers
numbers = [1, 2, 3, 4, 5, 6]
for num in numbers:
    if num % 2 == 0:
        continue  # Skip even numbers
    print("Odd number:", num)
# Output:
# Odd number: 1
# Odd number: 3
# Odd number: 5 
# --------------------------------------------------------------------------------
# Automation Example - Using break to stop test execution when a failure is encountered
tests = [
    "Login",
    "Search",
    "Payment",
    "Logout"
]

for test in tests:

    if test == "Payment":
        print("Failed")
        break

    print("Passed:", test)
# Output:
# Passed: Login
# Passed: Search
# Failed
# --------------------------------------------------------------------------------
# Nested Loops - A loop inside another loop. The inner loop runs completely for each iteration of the outer loop.
# Example: Print a multiplication table using nested loops
for i in range(1, 4):  # Outer loop for numbers 1 to 3
    for j in range(1, 4):  # Inner loop for numbers 1 to 3
        print(i * j, end=" ")  # Print product and stay on the same line
    print()  # Move to the next line after inner loop completes
# Output:
# 1 2 3 
# 2 4 6
# 3 6 9 
# --------------------------------------------------------------------------------
# Automation Example - Using nested loops to simulate testing multiple browsers with multiple test cases
browsers = ["Chrome", "Firefox"]
test_cases = ["Login Test", "Search Test"]  
for browser in browsers:
    print("Testing on:", browser)
    for test in test_cases:
        print("Executing:", test)   
# Output:
# Testing on: Chrome    
# Executing: Login Test
# Executing: Search Test   
# Testing on: Firefox
# Executing: Login Test     
# Executing: Search Test
# --------------------------------------------------------------------------------
# Automation Example - By above Example, we can see that we are testing 2 browsers with 2 test cases, which results in 4 total test executions. 
# Fail the TestCase "Search Test" on Firefox and use break to stop further execution on that browser and similarly pass the testcase in Chrome and continue to execute next test case on Firefox using continue statement.
browsers = ["Chrome", "Firefox"]
test_cases = ["Login Test", "Search Test"]
for browser in browsers:
    print("Testing on:", browser)
    for test in test_cases:
        if browser == "Firefox" and test == "Search Test":
            print("Failed:", test, "on", browser)
            break  # Stop further execution on Firefox
        elif browser == "Chrome" and test == "Search Test":
            print("Passed:", test, "on", browser)
            continue  # Continue to next test case on Firefox
        print("Executing:", test)   
# Output:
# Testing on: Chrome    
# Executing: Login Test
# Passed: Search Test on Chrome
# Testing on: Firefox
# Executing: Login Test
# Failed: Search Test on Firefox
# --------------------------------------------------------------------------------
#Reverse the above scenario by failing the testcase in Chrome and continue to execute next test case on Firefox using continue statement and similarly pass the testcase in Firefox and use break to stop further execution on that browser.
browsers = ["Chrome", "Firefox"]
test_cases = ["Login Test", "Search Test"]
for browser in browsers:
    print("Testing on:", browser)
    for test in test_cases:
        if browser == "Chrome" and test == "Search Test":
            print("Failed:", test, "on", browser)
            break  # Stop further execution on Chrome
        elif browser == "Firefox" and test == "Search Test":
            print("Passed:", test, "on", browser)
            continue  # Continue to next test case on Firefox
        print("Executing:", test)
# Output:
# Testing on: Chrome   
# Executing: Login Test
# Failed: Search Test on Chrome     
# Testing on: Firefox
# Executing: Login Test 
# Passed: Search Test on Firefox
#-----------------------------------------------------------------------------
# Print multiplication table of 5 using for loop
for i in range(1, 11):
    print("5 x", i, "=", 5 * i) 
# Output:
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# 5 x 4 = 20
# 5 x 5 = 25    
# 5 x 6 = 30
# 5 x 7 = 35
# 5 x 8 = 40
# 5 x 9 = 45
# 5 x 10 = 50
#-----------------------------------------------------------------------------
# Print above example using i j nested loop
for i in range(1, 6):
    for j in range(1, 11):
        print(i, "x", j, "=", i * j)
    print()  # Add a blank line after each table    
# Output:
# 1 x 1 = 1 
# 1 x 2 = 2
# 1 x 3 = 3
# 1 x 4 = 4
# 1 x 5 = 5
# 1 x 6 = 6
# 1 x 7 = 7
# 1 x 8 = 8
# 1 x 9 = 9
# 1 x 10 = 10
# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
# 2 x 4 = 8
# 2 x 5 = 10
# 2 x 6 = 12
# 2 x 7 = 14
# 2 x 8 = 16
# 2 x 9 = 18
# 2 x 10 = 20
# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9
# 3 x 4 = 12
# 3 x 5 = 15
# 3 x 6 = 18
# 3 x 7 = 21
# 3 x 8 = 24
# 3 x 9 = 27
# 3 x 10 = 30
# 4 x 1 = 4
# 4 x 2 = 8
# 4 x 3 = 12
# 4 x 4 = 16
# 4 x 5 = 20
# 4 x 6 = 24
# 4 x 7 = 28
# 4 x 8 = 32
# 4 x 9 = 36
# 4 x 10 = 40
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# 5 x 4 = 20
# 5 x 5 = 25
# 5 x 6 = 30
# 5 x 7 = 35
# 5 x 8 = 40
# 5 x 9 = 45
# 5 x 10 = 50
#-----------------------------------------------------------------------------
# Print multiplication table of 5 using while loop
num = 5
i = 1
while i <= 10:
    print(num, "x", i, "=", num * i)
    i += 1
# Output:
# 5 x 1 = 5
# 5 x 2 = 10       
# 5 x 3 = 15
# 5 x 4 = 20
# 5 x 5 = 25
# 5 x 6 = 30
# 5 x 7 = 35
# 5 x 8 = 40
# 5 x 9 = 45
# 5 x 10 = 50
#----------------------------------------------------------------------------
# Pass statement - used as placeholder with null operation - not much practical usage
for x in "Rahul":
    pass
# No Output is printed.
#----------------------------------------------------







