"""
Don't use regular expressions. In accordance with the assignment of your option, create a program for analyzing text entered from the keyboard

Lab: 3
Version: 1.0
Dev: Kuroedov Danila
Date: 24.03.2024

"""

def Task3():
    """Function for search words with first uppercase letter"""

    print("Введите строку: ")
    str1 = str(input())
    totalUpperCaseWords = 0

    for i in range(len(str1)):
        if str1[i] == str1[i].lower() and (i == 0 or str1[i - 1] == " ") and checkNumber(str1[i]) == False and checkConsonant(str1[i]) == True: # Consonant == согласный  
            totalUpperCaseWords += 1
        else:
            continue

    print(f"Количество слов, начинающиеся со строчной согласной буквы {totalUpperCaseWords}")

def checkConsonant(str1: str):
    """Function to check for consonant"""
    allGlasnyeBukvy = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я", "a", "e", "i", "o", "u", "y"]    

    isConsonant = True

    for i in range(len(allGlasnyeBukvy)):
        if str1 == allGlasnyeBukvy[i] or str1 == allGlasnyeBukvy[i].upper():
            isConsonant = False
        else:
            continue

    return isConsonant

def checkNumber(str1: str):
    """Function to check for number"""

    # nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    nums = [chr(48 + i) for i in range(0, 11)]

    isNumber = False

    if str1 in nums:
        isNumber = True
    
    return isNumber