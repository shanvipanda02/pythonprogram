# pythonprogram
What is a programming language ?

Programming language is used to process the data or instruction 

Python is a high-level, interpreted programming language known for its simplicity and readability. Here are some key features and uses

An interpreter is a program that executes code line-by-line, translating it directly into machine instructions at runtime.

A compiler is a program that translates the entire source code of a programming language into machine code before execution.
What is a token ?

In programming languages, a token is the smallest unit of meaningful data that the compiler or interpreter can process. 
Types of Tokens

**Keywords:** Reserved words that have a specific meaning in the language syntax.
Examples: if, while, return, class in languages like C++, Java, and Python.
Identifiers: Names given to various program elements such as variables, functions, arrays, etc.
Examples: myVariable, calculateSum, Student.
Operators: Symbols that represent operations to be performed.
Examples: +, -, *, /, =, ==.
Literals: Fixed values in the code.
Examples: 42 (integer literal), 3.14 (floating-point literal), 'c' (character literal), "Hello, World!" (string literal).
Separators (or Delimiters): Characters that separate tokens from each other.
Examples: , (comma), ; (semicolon), { (left brace), } (right brace), ( (left parenthesis), ) (right parenthesis).
Comments: Annotations in the code that are ignored by the compiler.
Examples: // This is a single-line comment (in C++, Java), /* This is a multi-line comment */
What is python instruction ?
A Python instruction is a single line of code that performs a specific action or operation in a Python program.

Python basic data types ?

1. Integer (int)
Represents whole numbers, positive or negative, without decimals.
2. Float (float)
Represents real numbers with a decimal point.
3. String (str)
Represents sequences of characters.
4. Boolean (bool)
Represents truth values: True or False.
NoneType (None)
Represents the absence of a value or a null value.


Python is a dynamically typed programming language. This means that you don't need to explicitly declare the data type of a variable when you assign a value to it.

Python interpreter - Collection of predefined syntaxes .
Memory  write operation 
x=10 
Memory Read Operation - 
X

In Python, operators are special symbols or keywords that perform operations on variables and values.

Arithmetic Operators
Arithmetic operators are used to perform mathematical operations.
Operator
Description
Example
+
Addition
x + y
-
Subtraction
x - y
*
Multiplication
x * y
/
Division
x / y
//
Floor Division
x // y
%
Modulus (Remainder)
x % y
**
Exponentiation
x ** y




Assignment Operators

Assignment operators are used to assign values to variables. Basically memory write operations 
Operator
Description
Example
=
Assign
x = 5
+=
Add and Assign
x += 5
-=
Subtract and Assign
x -= 5
*=
Multiply and Assign
x *= 5
/=
Divide and Assign
x /= 5
%=
Modulus and Assign
x %= 5
//=
Floor Division and Assign
x //= 5
**=
Exponentiation and Assign
x **= 5

Membership Operators

Membership operators are used to test if a sequence (e.g., string, list, tuple) contains a specific value.
Operator
Description
Example
in
True if value is found in sequence
5 in [1, 2, 3, 4, 5]
not in
True if value is not found in sequence
6 not in [1, 2, 3, 4, 5]

Identity Operators

Identity operators are used to compare the memory locations of two objects.
Operator
Description
Example
is
True if both variables point to the same object
x is y
is not
True if both variables do not point to the same object
x is not y

x = 10
y = 3

# Arithmetic operators

# Comparison operators
print(x == y)  # Output: False
print(x != y)  # Output: True
print(x > y)   # Output: True
print(x < y)   # Output: False
print(x >= y)  # Output: True
print(x <= y)  # Output: False

# Logical operators
print(x > 5 and y < 2)   # Output: False
print(x > 5 or y < 2)    # Output: True
print(not(x > 5 and y < 2))  # Output: True


Logical operators in Python are used to combine conditional statements. 
They are fundamental in making decisions based on multiple conditions.
 The primary logical operators in Python are and, or, and not.
and Operator
The and operator returns True if both statements are true.
Example:
x = 10
y = 20

if x > 5 and y > 15:
    print("Both conditions are true")  # Output: Both conditions are true
else:
    print("One or both conditions are false")

or Operator
The or operator returns True if at least one of the statements is true.
Example:
python
Copy code
x = 10
y = 5

if x > 5 or y > 15:
    print("At least one condition is true")  # Output: At least one condition is true
else:
    print("Both conditions are false")

not Operator
The not operator reverses the result, returns False if the result is true.
Example:
python
Copy code
x = False

if not x:
    print("x is False")  # Output: x is False
else:
    print("x is True")

Combining Logical Operators
Logical operators can be combined to form more complex conditions.
Example:
x = 10
y = 5
z = 15

if (x > 5 and y < 10) or z == 15:
    print("Complex condition is true")  # Output: Complex condition is true
else:
    print("Complex condition is false")

More Examples of Logical Operators
Example 1: Checking Multiple Conditions
age = 25
has_license = True
if age >= 18 and has_license:
    print("You can drive!")  # Output: You can drive!
else:
    print("You cannot drive.")

Example 2: Evaluating Multiple Logical Conditions
temperature = 100
humidity = 20

if temperature > 30 or humidity < 40:
    print("Extreme weather conditions!")  # Output: Extreme weather conditions!
else:
    print("Weather conditions are normal.")

Example 3: Using not for Negation
is_raining = False
if not is_raining:
    print("No need for an umbrella!")  # Output: No need for an umbrella!
else:
    print("Take an umbrella with you.")

Example 4: Nested Logical Conditions
score = 85
attendance = 90

if score > 80:
    if attendance > 85:
        print("Eligible for scholarship")  # Output: Eligible for scholarship
    else:
        print("Not eligible for scholarship due to low attendance.")
else:
    print("Not eligible for scholarship due to low score.")
In Python, operator precedence determines the order in which operators are evaluated in an expression. Operators with higher precedence are evaluated first. Here's a summary of operator precedence in Python, from highest to lowest:

Operator Precedence Rules
Parentheses (): Highest precedence; expressions within parentheses are evaluated first.
Exponentiation **: Second highest precedence.
Example: 2 ** 3 ** 2 is evaluated as 2 ** (3 ** 2).
Unary Operators +x, -x, ~x: These operators have the highest precedence among unary (single-operand) operators.
Multiplication *, Division /, Floor Division //, Modulus %: These operators have higher precedence than addition and subtraction.
Addition +, Subtraction -: Addition and subtraction have lower precedence than multiplication, division, and related operations.
Comparison Operators ==, !=, <, >, <=, >=, is, is not, in, not in: These operators compare values and have lower precedence than arithmetic and bitwise operators.
Boolean NOT not: Unary operator that has higher precedence than logical AND (and) and OR (or).
Boolean AND and: Logical AND operator that has higher precedence than logical OR.
Boolean OR or: Logical OR operator with the lowest precedence among logical operators.
Example of Operator Precedence
Consider the following example:
result = 10 + 5 * 2 / 3

To evaluate result:
5 * 2 is evaluated first, resulting in 10.
10 / 3 is then evaluated, resulting in approximately 3.3333.
Finally, 10 + 3.3333 is evaluated, resulting in 13.3333.
Explicit Use of Parentheses
You can use parentheses to override the default precedence and explicitly specify the order of evaluation:
result = (10 + 5) * 2 / 3

10 + 5 is evaluated first, resulting in 15.
15 * 2 is then evaluated, resulting in 30.
30 / 3 is evaluated last, resulting in 10.0.
Python mode of Execution 
1. Interactive Way
In Python, the interactive way typically refers to using the Python interpreter interactively.This mode allows you to enter Python commands or statements one at a time, and immediately see the results.
Using the Python Interpreter:
Open Terminal or Command Prompt:
Start a terminal or command prompt session on your computer.
Launch Python Interpreter:
Type python or python3 (depending on your Python installation) and press Enter.
Interact with Python:
Once in the interpreter, you can type Python statements directly:
python
Copy code
>>> print("Hello, World!")
Hello, World!
>>> x = 10
>>> x * 2
20
2. Declarative Way (Running Scripts)
The declarative way of running Python involves writing scripts in text files with the .py extension and then executing these scripts using the Python interpreter.
Running Python Scripts:
Create a Python Script:
Write your Python code in a text editor and save it with a .py extension. For example, my_script.py.
python my_script.py
int(): Converts a value to an integer.


x = int(3.14)  # x will be 3
y = int("42")  # y will be 42

float(): Converts a value to a float.


x = float(3)   # x will be 3.0
y = float("42.42")  # y will be 42.42

str(): Converts a value to a string.


x = str(3.14)  # x will be '3.14'
y = str(42)    # y will be '42'

bool(): Converts a value to a boolean.

x = bool(1)    # x will be True
y = bool(0)    # y will be False
z = bool("")   # z will be False


Python conditional statements are used to execute a block of code based on whether a condition is true or false. The main conditional statements in Python are if, elif, and else. Here's an overview of each:
Condition can be zero or non zero , null ,non null , true or false ,empty non empty 
If supportive non zero,
if statement:
Used to test a specific condition.
If the condition is true, the code block inside the if statement is executed.
Syntax:
if condition:
    # code to execute if condition is true


elif statement:
Stands for "else if".
Used to test another condition if the previous if condition is false.
Can have multiple elif statements to check different conditions.
Syntax:
if condition1:
    # code to execute if condition1 is true
elif condition2:
    # code to execute if condition1 is false and condition2 is true
elif condition3:
    # code to execute if condition1 and condition2 are false and condition3 is true


else statement:
Used as a catch-all block to execute code when none of the previous conditions are true.
Must be the last condition in the chain.
Syntax:
if condition1:
    # code to execute if condition1 is true
elif condition2:
    # code to execute if condition1 is false and condition2 is true
else:
    # code to execute if none of the above conditions are true


Example
Here’s a complete example that uses if, elif, and else statements:
age = 25

if age < 18:
    print("You are a minor.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

Explanation:
If age is less than 18, it prints "You are a minor."
If age is between 18 (inclusive) and 65 (exclusive), it prints "You are an adult."
If age is 65 or older, it prints "You are a senior citizen."
Points to Remember
Conditions in if, elif, and else statements are evaluated in order. Once a condition is found to be true, the corresponding block of code is executed, and the rest are skipped.
Indentation is crucial in Python. Each block of code under if, elif, or else must be indented.
Logical operators (and, or, not) can be used to combine multiple conditions.
Logical Operators Example
temperature = 75
humidity = 50

if temperature > 70 and humidity < 60:
    print("The weather is nice.")
else:
    print("The weather is not nice.")

In this example:
If both temperature > 70 and humidity < 60 are true, it prints "The weather is nice."
Otherwise, it prints "The weather is not nice."
Boolean Data type using python conditional statement 
Example 1: Check if the user is logged in
is_logged_in = True

if is_logged_in:
    print("Welcome back!")
else:
    print("Please log in.")

Example 2: Check if the store is open
is_store_open = False
if is_store_open:
    print("The store is open.")
else:
    print("The store is closed.")

Example 3: Check if the email is verified
is_email_verified = True

if is_email_verified:
    print("Email is verified.")
else:
    print("Email is not verified.")

Example 4: Check if the temperature is within a comfortable range
is_temperature_comfortable = False

if is_temperature_comfortable:
    print("The temperature is comfortable.")
else:
    print("The temperature is not comfortable.")

Example 5: Check if a file exists
file_exists = True
if file_exists:
    print("The file exists.")
else:
    print("The file does not exist.")
Using number 
Example 1: Check if a number is positive, negative, or zero
number = 5
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

Example 2: Check if a number is even or odd
python
Copy code
number = 8

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

Example 3: Determine the age group of a person
python
Copy code
age = 25

if age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
elif age < 60:
    print("You are an adult.")
else:
    print("You are a senior.")

Example 4: Compare two numbers
python
Copy code
a = 10
b = 20

if a > b:
    print("a is greater than b.")
elif a < b:
    print("a is less than b.")
else:
    print("a is equal to b.")

Example 5: Check if a number is within a specific range

number = 15
if number >= 10 and number <= 20:
    print("The number is within the range 10 to 20.")
else:
    print("The number is outside the range 10 to 20.")
Logical Operators Example
Example 1: Checking multiple conditions with and
age = 25
is_student = False

if age > 18 and not is_student:
    print("You are eligible to vote.")
else:
    print("You are either under 18 or a student.")

Example 2: Checking multiple conditions with or
temperature = 28
is_raining = True
if temperature > 30 or is_raining:
    print("It's either too hot or raining outside.")
else:
    print("Weather is fine.")

Example 3: Using not to negate a condition
python
Copy code
is_logged_in = False

if not is_logged_in:
    print("Please log in to continue.")
else:
    print("Welcome!")

Example 4: Combining and and or operators
age = 25
is_student = False
has_work_experience = True

if (age >= 18 and not is_student) or has_work_experience:
    print("You are eligible for the job.")
else:
    print("You do not meet the eligibility criteria.")


Example 5: Checking for a condition within a range
number = 15
if number < 10 or number > 20:
    print("The number is outside the range 10 to 20.")
else:
    print("The number is within the range 10 to 20.")
Python keywords
Python keywords are reserved words that have specific meanings and purposes in the language.

Example 1: Grade Evaluation
score = 85
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'
print(f"Your grade is {grade}")
Example 2: Nested Conditions for Age and License
age = 20
has_license = True

if age >= 18:
    if has_license:
        print("You can drive!")
    else:
        print("You need a driving license!")
else:
    print("You are too young to drive.")

age = 17
is_citizen = True
criminal_record = False

Example 3: Complex Voting Eligibility
if age >= 18 and is_citizen and not criminal_record:
    print("You are eligible to vote.")
elif age < 18:
    print("You are too young to vote.")
elif not is_citizen:
    print("You must be a citizen to vote.")
elif criminal_record:
    print("You cannot vote due to your criminal record.")

Example 4: Advanced Shopping Discount
purchase_amount = 150
membership_level = 'Gold'

if membership_level == 'Platinum':
    discount = 0.20
elif membership_level == 'Gold':
    discount = 0.15
elif membership_level == 'Silver':
    discount = 0.10
else:
    discount = 0.05

final_amount = purchase_amount * (1 - discount)
print(f"Final amount after discount: ${final_amount:.2f}")

Example 5: User Authentication
username = "admin"
password = "secret"

if username == "admin":
    if password == "secret":
        print("Access granted")
    else:
        print("Incorrect password")
else:
    print("Unknown user")

Example 6: Loan Approval Process
age = 30
income = 50000
credit_score = 700

if age >= 18:
    if income >= 40000:
        if credit_score >= 650:
            print("Loan approved")
        else:
            print("Loan denied due to low credit score")
    else:
        print("Loan denied due to insufficient income")
else:
    print("Loan denied due to age")

Example 7: Complex Pricing Strategy
customer_type = "VIP"
total_purchase = 200

if customer_type == "VIP":
    if total_purchase > 500:
        discount = 0.30
    elif total_purchase > 300:
        discount = 0.20
    else:
        discount = 0.10
elif customer_type == "Regular":
    if total_purchase > 500:
        discount = 0.15
    elif total_purchase > 300:
        discount = 0.10
    else:
        discount = 0.05
else:
    discount = 0.02

final_price = total_purchase * (1 - discount)
print(f"Final price: ${final_price:.2f}")

Example 10: Traffic Light System
light_color = "green"
pedestrian_crossing = False

if light_color == "green":
    if pedestrian_crossing:
        print("Wait for pedestrians to cross")
    else:
        print("Go")
elif light_color == "yellow":
    if pedestrian_crossing:
        print("Prepare to stop and wait for pedestrians")
    else:
        print("Prepare to stop")
elif light_color == "red":
    print("Stop")
else:
    print("Invalid light color")

Real Estate Business Example
# Information about the property and buyer
property_type = "house"  # Can be "house", "apartment", "commercial"
property_price = 300000
buyer_budget = 350000
has_pre_approval = True
credit_score = 720
financing_option = "loan"  # Can be "loan", "cash", "lease"

# Determine eligibility and recommendations
if buyer_budget >= property_price:
    if financing_option == "cash":
        print("Buyer can purchase the property with cash.")
    elif financing_option == "loan":
        if has_pre_approval:
            if credit_score >= 700:
                print("Buyer is eligible for a loan. Proceed with the purchase.")
            elif credit_score >= 650:
                print("Buyer might get a loan with a higher interest rate.")
            else:
                print("Buyer needs to improve their credit score to get a loan.")
        else:
            print("Buyer needs pre-approval to proceed with the loan.")
    elif financing_option == "lease":
        if property_type == "commercial":
            print("Commercial property can be leased. Proceed with lease agreement.")
        else:
            print("Leasing option is not available for this property type.")
    else:
        print("Invalid financing option.")
else:
    if buyer_budget >= 0.9 * property_price:
        if financing_option == "loan":
            print("Buyer may qualify for a loan with a larger down payment.")
        else:
            print("Recommend the buyer to consider financing options to increase their budget.")
    else:
        print("Buyer needs to increase their budget or consider a less expensive property.")

# Additional recommendations based on property type
if property_type == "house":
    print("Recommend a home inspection before purchase.")
    if buyer_budget >= 1.1 * property_price:
        print("Suggest considering home improvement or renovation after purchase.")
elif property_type == "apartment":
    print("Check the HOA fees and regulations.")
    if buyer_budget >= 1.05 * property_price:
        print("Suggest purchasing an apartment with better amenities or a better location.")
elif property_type == "commercial":
    print("Verify zoning laws and business permits.")
    if buyer_budget >= 1.2 * property_price:
        print("Suggest considering additional commercial properties for investment.")
else:
    print("Invalid property type.")





String Methods
Conversion Methods:
str.upper(): Converts all characters in the string to uppercase.
str.lower(): Converts all characters in the string to lowercase.
str.capitalize(): Capitalizes the first character of the string.
str.title(): Converts the first character of each word to uppercase and the rest to lowercase.
Trimming Methods:
str.strip(): Removes leading and trailing whitespace characters from the string.
str.lstrip(): Removes leading whitespace characters.
str.rstrip(): Removes trailing whitespace characters.
Search and Replace Methods:
str.find(substring): Returns the lowest index where the substring is found (-1 if not found).
str.index(substring): Returns the lowest index where the substring is found (raises an exception if not found).
str.replace(old, new): Replaces occurrences of old substring with new substring.
str.count(substring): Returns the number of occurrences of substring in the string.
Splitting and Joining Methods:
str.split(sep=None, maxsplit=-1): Splits the string into a list of substrings using sep as the delimiter.
str.rsplit(sep=None, maxsplit=-1): Splits the string from the right end.
str.join(iterable): Joins elements of iterable into a single string using str as the separator.
Checking Methods:
str.startswith(prefix): Checks if the string starts with the specified prefix.
str.endswith(suffix): Checks if the string ends with the specified suffix.
str.isalpha(): Returns True if all characters in the string are alphabetic.
str.isdigit(): Returns True if all characters in the string are digits.
str.isalnum(): Returns True if all characters in the string are alphanumeric.
str.isspace(): Returns True if all characters in the string are whitespace.
Formatting Methods:
str.format(): Formats the string into a more readable output.
Formatted string literals or f-strings (introduced in Python 3.6):
python
Copy code
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")


Encoding and Decoding Methods:
str.encode(encoding='utf-8', errors='strict'): Returns the encoded version of the string as a bytes object.
bytes.decode(encoding='utf-8', errors='strict'): Decodes the bytes object into a string using the specified encoding.
Example Usage
Here’s an example demonstrating the use of some of these methods:
python
Copy code
my_string = "  Hello, World!  "

# Conversion methods
print(my_string.upper())       # '  HELLO, WORLD!  '
print(my_string.strip())      # 'Hello, World!'
print(my_string.replace('Hello', 'Hi'))  # '  Hi, World!  '

# Splitting and joining methods
print(my_string.split(','))   # ['  Hello', ' World!  ']
print('-'.join(['Hello', 'World']))  # 'Hello-World'

# Checking methods
print(my_string.startswith('  '))  # True
print(my_string.endswith('!  '))   # True
print(my_string.isalpha())         # False (contains non-alphabetic characters)






