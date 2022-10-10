from xmlrpc.client import boolean


def findNumber():
    string = input("Enter the string: ")

    number = ""
    hasStarted = 0
    for l in string:
        if l.isdigit():
            if hasStarted == 0:
                hasStarted = 1
            number = number + l
        else:
            if hasStarted == 1:
                break
    print(number)
