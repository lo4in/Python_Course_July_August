##  **Lesson 1 — Introduction to Python and Development Environment Setup**

###  **Learning Objectives**

By the end of this session, the student will be able to:

* Understand what Python is and where it is used.
* Install Python and Visual Studio Code (VS Code).
* Register and set up a GitHub account.
* Install Git on their computer.
* Upload files to a GitHub repository using Git.

---

##  **Lesson Outline**

### 1.  **What is Python?**

**Definition:**
Python is a high-level, interpreted programming language known for its readability and simplicity.

**Key Features:**

* Easy to read and write
* Dynamically typed
* Large standard library
* Community support
* Used in data science, web development, automation, AI, and more

**Real-World Applications:**

* Google uses Python for AI and backend services
* Netflix uses Python for data analysis
* Instagram backend is built with Django (a Python web framework)

---

### 2.  **Installing Python**

**Steps:**

1. Go to the official Python website: [https://www.python.org](https://www.python.org)
2. Click on **Downloads** and choose the appropriate version for your OS (e.g., Windows, macOS).
3. During installation, **check the box** that says *"Add Python to PATH"*.
4. Open Terminal or Command Prompt and type:

   ```bash
   python --version
   ```

   If installed correctly, it will show the version (e.g., `Python 3.12.1`)

---

### 3.  **Installing Visual Studio Code (VS Code)**

**Steps:**

1. Go to [https://code.visualstudio.com](https://code.visualstudio.com)
2. Download and install for your OS.
3. Open VS Code and install the **Python Extension**:

   * Go to the **Extensions** panel (or press `Ctrl+Shift+X`)
   * Search for `Python` and install the extension by Microsoft.

---

### 4.  **Setting Up Git and GitHub**

#### a.  **Creating a GitHub Account**

1. Go to [https://github.com](https://github.com)
2. Click **Sign up**
3. Fill in your email, password, and username
4. Verify your email

#### b. ⚙️ **Installing Git**

1. Go to [https://git-scm.com](https://git-scm.com)
2. Download the installer for your OS and install Git
3. Open Terminal and verify installation:

   ```bash
   git --version
   ```

#### c.  **Configuring Git**

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

---

### 5. ☁️ **Creating and Uploading to a GitHub Repository**

#### a.  Create a New Repository:

1. Go to your GitHub profile
2. Click on **Repositories** > **New**
3. Fill in:

   * Repository name
   * Description (optional)
   * Set it to **Public** or **Private**
   * Click **Create Repository**

#### b.  Clone the Repository to Your Computer:

```bash
git clone https://github.com/yourusername/repository-name.git
```

#### c.  Add Your Python Files:

1. Create or move your Python files into the cloned repository folder.

#### d. Commit and Push:

```bash
cd repository-name
git add .
git commit -m "Initial commit"
git push origin main
```

---

##  **Homework / Practice**

* Install Python and VS Code
* Create a GitHub account
* Push a simple Python file to your GitHub repo (e.g., `hello.py`)

---

##  **Resources**

* Python Docs: [https://docs.python.org/3/](https://docs.python.org/3/)
* GitHub Docs: [https://docs.github.com](https://docs.github.com)
* VS Code Docs: [https://code.visualstudio.com/docs](https://code.visualstudio.com/docs)
* Git Handbook: [https://git-scm.com/book/en/v2](https://git-scm.com/book/en/v2)

