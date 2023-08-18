#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def get_coordinates(self):
        return self.x, self.y, self.z

my_point = Point3D(1, 2, 3)

print(my_point.get_coordinates())


# In[2]:


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

my_rectangle = Rectangle(4, 3)

area = my_rectangle.area()
perimeter = my_rectangle.perimeter()

print("Area:", area)
print("Perimeter:", perimeter)


# In[3]:


import math

class Circle:
    def __init__(self, center_x, center_y, radius):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius
        
    def area(self):
        return math.pi * self.radius**2
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
    def is_inside(self, x, y):
        distance_squared = (x - self.center_x)**2 + (y - self.center_y)**2
        return distance_squared <= self.radius**2

my_circle = Circle(0, 0, 5)

area = my_circle.area()
perimeter = my_circle.perimeter()

print("Area:", area)
print("Perimeter:", perimeter)

print("(2, 2) is inside the circle:", my_circle.is_inside(2, 2))
print("(6, 6) is inside the circle:", my_circle.is_inside(6, 6))


# In[4]:


class Bank:
    def __init__(self, balance):
        self.balance = balance
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid deposit amount"
        
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        else:
            return "Insufficient funds or invalid withdrawal amount"

initial_balance = 1000
account = Bank(initial_balance)


print(account.deposit(500))
print(account.withdraw(200))
print(account.withdraw(1500))


# In[ ]:




