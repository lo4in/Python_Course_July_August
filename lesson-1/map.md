
# **Lesson 1: Introduction to Python and Development Environment Setup**

## **Learning Objectives**

By the end of this session, the student will be able to:

* Understand what Python is and its real-world applications.
* Install Python and Visual Studio Code.
* Create a GitHub account and configure Git.
* Push code to a GitHub repository.
* Write basic Python code using variables, data types, input/output, and expressions.

---

## **1. What is Python?**

**Definition:**
Python is a high-level, interpreted programming language known for its readability and versatility.

**Key Features:**

* Simple and readable syntax
* Dynamically typed
* Extensive standard libraries
* Strong community support

**Applications:**

* Web development (Django, Flask)
* Data science and machine learning (pandas, NumPy, scikit-learn)
* Automation and scripting
* Game development
* Desktop applications

---

## **2. Installing Python**

**Steps:**

1. Visit the official Python website: [https://www.python.org](https://www.python.org)
2. Navigate to the "Downloads" section and select your operating system.
3. Download and run the installer.
4. During installation, make sure to check the box “Add Python to PATH”.
5. After installation, verify using terminal:

   ```bash
   python --version
   ```

---

## **3. Installing Visual Studio Code (VS Code)**

**Steps:**

1. Go to [https://code.visualstudio.com](https://code.visualstudio.com)
2. Download the installer for your operating system and install it.
3. Launch VS Code and open the Extensions panel (or press `Ctrl+Shift+X`).
4. Search for "Python" and install the extension by Microsoft.
5. Optionally, install the "GitHub Copilot" and "Pylance" extensions for assistance.

---

## **4. Basic Python Programming**

### 4.1 Printing Output

```python
print("Hello, world!")
print("Welcome to Python programming.")
```

### 4.2 Variables and Data Types

```python
name = "Alice"       # str
age = 25             # int
height = 1.68        # float
is_student = True    # bool
```

### 4.3 Numeric Operations

```python
a = 10
b = 3

print(a + b)     # Addition
print(a - b)     # Subtraction
print(a * b)     # Multiplication
print(a / b)     # Division (float)
print(a // b)    # Integer division
print(a % b)     # Modulus
print(a ** b)    # Exponentiation
```

### 4.4 Getting User Input

```python
name = input("What is your name? ")
print("Hello, " + name + "!")
```

All inputs are strings by default.

### 4.5 Type Conversion

```python
age = input("Enter your age: ")
age = int(age)
print("You will be", age + 1, "next year.")
```

Other common conversions:

* `int()`
* `float()`
* `str()`
* `bool()`

---

### 4.6 Practice Exercises

**Exercise 1: Greeting**

```python
name = input("Enter your name: ")
print("Hello,", name)
```

**Exercise 2: Age Calculator**

```python
birth_year = int(input("Enter your birth year: "))
current_year = 2025
print("Your age is:", current_year - birth_year)
```

**Exercise 3: Rectangle Perimeter**

```python
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
perimeter = 2 * (length + width)
print("Perimeter:", perimeter)
```

**Exercise 4: Simple Calculator**

```python
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Sum:", a + b)
print("Product:", a * b)
```

---

## **5. Creating a GitHub Account**

**Steps:**

1. Go to [https://github.com](https://github.com)
2. Click "Sign up"
3. Choose a username, enter your email and password
4. Complete email verification

---

## **6. Installing Git**

**Steps:**

1. Visit [https://git-scm.com](https://git-scm.com)
2. Download and install Git for your operating system
3. Verify installation:

   ```bash
   git --version
   ```

**Basic Configuration:**

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

---

## **7. Uploading Code to GitHub**

### a. Create a New Repository:

1. On GitHub, go to your profile → "Repositories" → "New"
2. Name the repository and set visibility
3. Click "Create repository"

### b. Clone the Repository:

```bash
git clone https://github.com/yourusername/your-repository.git
```

### c. Add Your Files:

Move your Python files into the cloned folder, then:

```bash
cd your-repository
git add .
git commit -m "Initial commit"
git push origin main
```

---

## **Homework / Self-Practice**

* Install Python and VS Code on your machine
* Complete the exercises from section 4
* Create a GitHub account
* Upload your Python files to your repository

---

## **References**

* Official Python Docs: [https://docs.python.org/3/](https://docs.python.org/3/)
* VS Code Docs: [https://code.visualstudio.com/docs](https://code.visualstudio.com/docs)
* Git Handbook: [https://git-scm.com/book/en/v2](https://git-scm.com/book/en/v2)
* GitHub Docs: [https://docs.github.com](https://docs.github.com)


