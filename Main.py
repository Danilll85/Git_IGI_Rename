import math
from Task1 import Task1
from Task2 import Task2
from Task3 import Task3
from Task4 import Task4
from Task5 import Task5

print("Выберите номер задания(1 - 5): ")
choice = int(input())

switch = {1: Task1,
          2: Task2,
          3: Task3,
          4: Task4,
          5: Task5}


if choice in switch:
    switch[choice]()
else:
    "Неправильный выбор"
