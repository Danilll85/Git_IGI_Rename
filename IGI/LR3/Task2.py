"""
In accordance with the assignment of your option, create a program to find the sum of a sequence of numbers

Lab: 3
Version: 1.0
Dev: Kuroedov Danila
Date: 24.03.2024

"""

import math

def decorator(func):
    def wrapper():    
        print("Введите целые числа для их суммирования (для выхода из программы введите число > 100)")
        
        func()
    
    return wrapper

@decorator
def Task2():
    """Function for summing integers"""
    total = 0

    while True:
        num = int(input())

        if num > 100:
            break
        else:
            total += num
        
    print("Сумма введённых чисел - {}".format(total))
        