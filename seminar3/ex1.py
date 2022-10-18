def fibonacci(nr):
    toReturnList = [0, 1]
    if nr <= 0:
        print("No values to be shown. Enter a value greater than 0.")
    else:
        k = min(2, nr)
        while k < nr:
            toReturnList.append(toReturnList[k-1]+toReturnList[k-2])
            k = k+1
    return toReturnList[0:k]


nr = int(input("Enter your value:"))
print(fibonacci(nr))
