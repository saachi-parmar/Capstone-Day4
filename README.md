# Capstone-Day4

## 📘 Introduction to OOPS in Python

This repository contains basic implementations of **Object-Oriented Programming (OOP)** concepts in Python.  
It covers **Abstraction**, **Encapsulation**, **Inheritance**, and **Polymorphism** through simple, beginner-friendly examples.

---

### 🧠 Concepts Covered

1. **Abstraction**  
2. **Encapsulation**  
3. **Inheritance**  
4. **Polymorphism**

---

### 📝 What These Topics Mean

- **Abstraction**  
  - Abstraction hides the internal implementation and shows only essential features.  
  - 🧪 **Example**: An abstract class `Payment` and a subclass `CreditCardPayment` overriding the method.  
  - The subclass provides an implementation for the abstract method `process_payment()`.

- **Encapsulation**  
  - Encapsulation wraps data and functions into a single unit and restricts direct access to some components.  
  - 🧪 **Example**: Private salary attribute with getter/setter in `Employee`, and banking logic in `BankAccount`.  
  - Demonstrates bundling data with methods using private attributes and controlled access through getters/setters.

- **Inheritance**  
  - Inheritance allows one class to inherit attributes and methods from another.  
  - 🧪 **Example**: `Dog` and `Cat` inherit from `Animal`, `Child` inherits from `Father` and `Mother`, etc.  
  - Includes:
    - **Single Inheritance**: `Dog`, `Cat` → `Animal`  
    - **Multiple Inheritance**: `Child` → `Father`, `Mother`  
    - **Multilevel Inheritance**: `Child` → `Parent` → `Grandparent`  
    - **MRO (Method Resolution Order)**: Demonstrated using class `C` from `A`, `B`, and `Base`.

- **Polymorphism**  
  - Polymorphism allows the same method name to behave differently in different classes.  
  - 🧪 **Example**: `area()` behaves differently in `Circle` and `Rectangle`.  
  - Each class implements its own version of the method suited to its needs.

---

### ✅ Code-to-Concept Mapping

| Concept        | Example Classes/Methods                                  |
|----------------|----------------------------------------------------------|
| Abstraction    | `Payment`, `CreditCardPayment.process_payment()`         |
| Encapsulation  | `Employee` (private `__salary`), `BankAccount`           |
| Inheritance    | `Dog`, `Cat`, `Child`, `Parent`, `Grandparent`, `C`      |
| Polymorphism   | `Circle.area()`, `Rectangle.area()`                      |

---

💡 **Explore the code files to see each concept in action.**  
Perfect for beginners looking to understand core OOP principles in Python!
