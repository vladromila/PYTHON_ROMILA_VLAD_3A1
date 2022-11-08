def argSum(**kwArgs):
    sum = 0
    for kw in kwArgs.keys():
        sum += int(kwArgs[kw])
    return sum


aFunction = lambda **kwArgs: sum([val for val in kwArgs.values()])
print(aFunction(a=1, b=2, c=3))
