"""
In accordance with the instructions of your option, create a program for processing real lists. The program must contain the following basic functions:
Lab: 3
Version: 1.0
Dev: Kuroedov Danila
Date: 24.03.2024

"""

def Task5():
    arr = list(map(float, input("Введите элементы списка через пробел: ").split()))

    zeros = countZeros(arr)

    sumOfAbs = sumAfterMinAbs(arr)

    print(f"Кол-во элементов списка равных нулю {zeros}")

    print(f"Сумма элементов списка после минимального по модулю элемента {sumOfAbs}")

def countZeros(arr: list):
    """Function to count the number of list elements equal to 0."""
    count = 0
    
    for i in range(len(arr)):
        if arr[i] == 0.0:
            count += 1
        else:
            continue

    return count

def sumAfterMinAbs(arr: list):
    minIndex = arr.index(min(arr, key=abs))

    sumAfterMin = sum(arr[minIndex + 1:])

    return sumAfterMin