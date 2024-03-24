'''
Task 1. Program to calculate the value of a function using a power series expansion with a given accuracy eps. 
The maximum number of iterations is 500. Output the number of terms of the series for the specified accuracy. 
Present the result in the form of a table.

Lab: 3
Version: 1.0
Dev: Kuroedov Danila
Date: 24.03.2024
'''


import math
from prettytable import PrettyTable

def Task1():
    """Function for input values"""

    print('Введите x: ')
    x = int(input())

    print('Введите желаемую точность eps: ')
    eps = float(input())

    createTable(F(x,eps))

def mathF(x):
    """Function for calculating a series using the library math"""

    return math.exp(x)

def F(x, eps):
    """Function for calculating series manually"""

    res = 0
    n = 0
    arr = []
    while (abs(mathF(x) - res) > eps):
        if n <= 500:
            res += (x**n) / math.factorial(n)
            arr.extend([x, n , res, mathF(x), eps])
            n += 1
        else:
            break

    return arr

def createTable(arr: list):
    """Function to create a table"""

    title = ['x', 'n', 'F(x)', 'Math F(x)', 'eps']
    cols = len(title)
    table = PrettyTable(title)

    for _ in range(len(arr) // cols):
        table.add_row(arr[:cols])
        arr = arr[cols:]

    print(table)



    
        
