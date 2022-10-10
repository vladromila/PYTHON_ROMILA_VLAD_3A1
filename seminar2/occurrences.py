def findOccurrencesV():
    numberOfOccurrences = 0
    firstString = input("Your first string: ")
    secondString = input("Your second string: ")
    firstString = firstString.lower()
    secondString = secondString.lower()
    for i in range(0, min(len(firstString), len(secondString))):
        if firstString[i] == secondString[i]:
            numberOfOccurrences += 1
    print(numberOfOccurrences)


def findOccurrencesV2(str1, str2):
    count = 0
    flag = True
    start = 0

    while flag:
        a = str2.find(str1, start)
        if a == -1:
            flag = False
        else:
            count += 1
            start = a + 1
    print(count)
