# Lesson 2: Python Data Types – String and Numeric Methods; if/else Statements

## Learning Objectives

By the end of this session, the student will be able to:

* Understand and apply common methods for string and numeric data types
* Use conditional logic with `if`, `elif`, and `else`
* Apply boolean operators in decision-making
* Write programs that validate user input and handle simple decision branches

---

## 1. String Methods in Python

**Common String Methods:**

```python
text = "  Hello, World!  "

print(text.lower())          # '  hello, world!  '
print(text.upper())          # '  HELLO, WORLD!  '
print(text.capitalize())     # '  hello, world!  '
print(text.strip())          # 'Hello, World!'
print(text.replace("World", "Python"))  # '  Hello, Python!  '
print(text.startswith("  He"))  # True
print(text.endswith("!  "))    # True
print(len(text))             # 17
```

**Example Task:**

```python
sentence = input("Enter a sentence: ")
print("Lowercase:", sentence.lower())
print("Words count:", len(sentence.strip().split()))
```

---

## 2. Numeric Methods and Functions

**Built-in Numeric Functions and Usage:**

```python
x = -8
y = 3.14159

print(abs(x))        # 8
print(round(y))      # 3
print(round(y, 2))   # 3.14
print(pow(2, 5))     # 32
```

**Math Module:**

```python
import math

number = 25
print(math.sqrt(number))    # 5.0
print(math.floor(3.9))       # 3
print(math.ceil(3.1))        # 4
print(math.pi)               # 3.141592653589793
```

**Example Task:**

```python
import math
r = float(input("Enter the radius of a circle: "))
area = math.pi * r ** 2
circumference = 2 * math.pi * r
print(f"Area: {round(area, 2)}")
print(f"Circumference: {round(circumference, 2)}")
```

---

## 3. if / elif / else Statements

**Syntax Overview:**

```python
if condition:
    # block 1
elif another_condition:
    # block 2
else:
    # block 3
```

**Example 1: Simple Comparison**

```python
x = int(input("Enter a number: "))
if x > 0:
    print("The number is positive.")
elif x < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
```

**Example 2: Grade Classifier**

```python
score = int(input("Enter your exam score (0–100): "))
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
```

---

## 4. Boolean Logic and Operators

**Logical Operators:**

* `and`: both conditions must be true
* `or`: at least one must be true
* `not`: reverses boolean value

**Example:**

```python
age = int(input("Enter your age: "))
is_student = input("Are you a student? (yes/no): ").lower() == "yes"

if age >= 18 and is_student:
    print("You qualify for a student discount.")
else:
    print("No discount available.")
```

**Using `not`**

```python
name = input("Enter your name: ")
if not name:
    print("You did not enter a name.")
else:
    print(f"Hello, {name}!")
```

---

## 5. Using `in` and `not in` with Strings

**Example:**

```python
email = input("Enter your email: ")
if "@" in email and "." in email:
    print("This looks like a valid email address.")
else:
    print("Invalid email format.")
```

**Another Example:**

```python
bad_chars = "$%#&"
password = input("Enter a password: ")
if any(char in password for char in bad_chars):
    print("Password contains forbidden characters.")
else:
    print("Password accepted.")
```

---

## 6. Nested if Statements

**Example:**

```python
age = int(input("Enter your age: "))
if age >= 18:
    citizen = input("Are you a citizen? (yes/no): ").lower()
    if citizen == "yes":
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")
else:
    print("You must be at least 18 years old to vote.")
```

---

## 7. Practice Exercises with Solutions

### Exercise 1: Username Validator

**Task:** Ask the user to enter a username. If it starts with a capital letter and is at least 5 characters long, print "Valid"; otherwise, print "Invalid".

```python
username = input("Enter a username: ")
if username and username[0].isupper() and len(username) >= 5:
    print("Valid")
else:
    print("Invalid")
```

### Exercise 2: Even or Odd Checker

```python
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```

### Exercise 3: Password Strength Checker

```python
password = input("Enter password: ")
if (len(password) >= 8 and
    any(c.isdigit() for c in password) and
    any(c.islower() for c in password) and
    any(c.isupper() for c in password)):
    print("Strong")
else:
    print("Weak")
```

### Exercise 4: Ticket Price Calculator

```python
age = int(input("Enter your age: "))
if age < 12 or age >= 60:
    print("You get a discounted ticket.")
else:
    print("Regular ticket price applies.")
```

---

## Homework / Self-Practice

* Write a program that asks for a string and prints the number of vowels.
* Ask the user to input a number and print whether it is divisible by 3 and 5.
* Ask for name and age. If age is under 18, print "Minor", else "Adult".
* Ask for a password and ensure it does not contain spaces and is at least 10 characters long.

---

## References

* Python String Methods: [https://docs.python.org/3/library/stdtypes.html#string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
* Python Math Library: [https://docs.python.org/3/library/math.html](https://docs.python.org/3/library/math.html)
* Conditional Statements: [https://docs.python.org/3/tutorial/controlflow.html](https://docs.python.org/3/tutorial/controlflow.html)
