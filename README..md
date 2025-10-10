# 🐍 Python Mastery Journey

Welcome to my **Python Mastery Journey** — a hands-on coding practice repo where I document everything I learn while mastering Python.

## 🚀 About This Repository

This repo contains my Python learning assignments, challenges, and mini-projects.  
Every file here represents a step forward — from basic syntax to real-world projects.

## 📘 Current Focus
- Building a strong foundation in **Python programming**
- Mastering **problem solving** and **clean code practices**
- Learning by doing — through coding exercises, assignments, and collaboration

## 💡 What You’ll Find Here
- 🔢 **Beginner Projects** — simple calculator, loops, conditionals, etc.  
- ⚙️ **Logic-Based Tasks** — pattern printing, number analysis, data handling  
- 🧠 **Future Goals** — data analysis, web development, and automation scripts  

## 🛠️ Tech Stack
- **Language:** Python 🐍  
- **Editor:** VS Code  
- **Version Control:** Git & GitHub  

## 🧩 Example Project
**Simple Python Calculator**
```python
while True:
    num1 = float(input('Enter first number: '))
    num2 = float(input('Enter second number: '))
    operation = input('Enter operation (+, -, *, /): ')

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2
    else:
        print("Invalid operation.")
        continue

    print(f'Result: {result}')
    again = input('Do another? (yes/no): ').lower()
    if again != 'yes':
        print("Goodbye!")
        break
