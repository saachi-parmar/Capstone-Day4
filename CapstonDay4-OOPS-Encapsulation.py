# Binding data into single unit

# Encapsulation refers to bundling data and methods that operate 
# on the data within one unit, typically a class.

# KEY POINTS:
# 1. Data Hiding- Use private (_var) and protected (_var) attribute 
# to restrict direct access.
# 2. Getters and Setters- Provide controlled access to private 
# attributes.

# ------------------------------------------------------------------
# Encapsulation ----------------------------------------------------

class Employee:
    def __init__(self, name, salary):
        self.name = name                       # Public attribute
        self.__salary = salary                 # Private attribute
        
    def get_salary(self):                      # Getter
        return self.__salary
    
    def set_salary(self, salary):              # Setter
        if salary > 0:
            self.__salary = salary
        else:
            print("Invalid Salary")
            
            
print('\n')
# -------------------------------------------------------------------
class BankAccount:
    def __init__(self, account_details, balance):
        self.account_details = account_details
        self.__balance = balance
        
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient Funds.")
            
    def get_balance(self):
        return self.__balance
    
account = BankAccount("Saachi", 1000)
account.deposit(5000)

print(account.get_balance())        