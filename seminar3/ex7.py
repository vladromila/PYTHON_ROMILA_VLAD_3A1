def isPalindrome(x):
    xCopy = int(str(x)[::-1])
    if x == xCopy:
        return True
    return False


def findPalindromes(list):
    maxValue = 0
    numberOfPalindromes = 0
    for el in list:
        if isPalindrome(el) == True:
            numberOfPalindromes += 1
            if maxValue < el:
                maxValue = el
    return (numberOfPalindromes, maxValue)


list = [121, 1122211, 11233211, 123322, 321123, 333331, 1244334]
print(findPalindromes(list))
