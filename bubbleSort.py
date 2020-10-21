import random

def generateRandomList(length):
    newList = []
    for i in range(0, length):
        n = random.randint(1, 99)
        newList.append(n);
    return newList

def bubbleSort(listLength):
    randList = generateRandomList(listLength)
    print(randList)
    for listLengthIndex in range(len(randList)-1):
        for index in range(0, listLength-listLengthIndex-1):
            if randList[index] > randList[index+1]:
                swap = randList[index]
                randList[index] = randList[index+1]
                randList[index+1] = swap

    print('\nSorted:')
    print(randList)

bubbleSort(15)