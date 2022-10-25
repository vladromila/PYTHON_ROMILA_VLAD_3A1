def valueCounter(*posVariables, **kwArguments):
    toReturnCounter = 0
    for posVar in posVariables:
        for (key, value) in kwArguments.items():
            if posVar == value:
                toReturnCounter += 1
                break
    return toReturnCounter


print(valueCounter(1, 2, 3, 4, x=1, y=2, z=3, w=5))
