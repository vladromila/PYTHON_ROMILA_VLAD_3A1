def my_function(l):
    toReturnList = []
    for el in l:
        if type(el) in [int, float, complex]:
            toReturnList.append(el)
    return toReturnList


print(my_function([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))
