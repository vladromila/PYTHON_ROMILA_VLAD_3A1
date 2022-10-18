
import math


def is_prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if (n % i) == 0:
            return False
    return True


def getPrimeElements(list):
    toReturnList = []

    for el in list:
        if is_prime(el) == True:
            toReturnList.append(el)
    return toReturnList


list = []

n = int(input("Enter number of elements in list: "))

for i in range(0, n):
    el = int(input())
    list.append(el)

print(getPrimeElements(list))
