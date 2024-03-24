"""
Given a line of text in which words are separated by spaces and commas. In accordance with the specification of your option, create a program to analyze the string initialized in the program code

Lab: 3
Version: 1.0
Dev: Kuroedov Danila
Date: 24.03.2024
"""

def Task4():
    testStr = "So she was considering in her own mind, as well as she could, for the hot day made her feel very sleepy and stupid, whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her."
    
    countOfMaxLenWords = countWordsWithMaxLen(testStr)
    allWordsWithDotsAndСommas = allWords(testStr)
    findMaxLenWordWithEOnTheEnd = findMaxE(testStr)

    print(f"Количество слов с максимальной длиной - {countOfMaxLenWords}")
    print(f"Слова имеющие на конце . или , - {allWordsWithDotsAndСommas}")
    print(f"Самое длинное слово, заканчивающееся на e - {findMaxLenWordWithEOnTheEnd}")


def countWordsWithMaxLen(str1: str):
    maxLetters = 0
    countofWords = 0

    str1 = str1.split(" ")

    for i in range(len(str1)):
        if maxLetters < len(str1[i]):
            maxLetters = len(str1[i])
        else:
            continue
    
    for i in range(len(str1)):
        if maxLetters == len(str1[i]):
            countofWords += 1
        else:
            continue
    
    return countofWords

def allWords(str1: str):
    words = []

    str1 = str1.split(" ")

    for i in range(len(str1)):
        if str1[i][-1] in {'.', ','}:
            words.append(str1[i])
        else:
            continue
    

    return words

def findMaxE(str1: str):
    words = []

    str1 = str1.split(" ")

    for word in str1:
        if word.endswith("e"):
            words.append(word)
        else:
            continue
    
    maxLenWord = str1[0] 

    for word in words:
        if len(maxLenWord) < len(word):
            maxLenWord = word
        else:
            continue
    
    return maxLenWord