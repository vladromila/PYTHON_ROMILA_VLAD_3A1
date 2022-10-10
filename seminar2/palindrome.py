def isPalindrome():
    x = int(input("Your number: "))
    xCopy = int(str(x)[::-1])
    if x == xCopy:
        print("The number is a palindrome.")
    else:
        print("The number is not a palindrome.")
