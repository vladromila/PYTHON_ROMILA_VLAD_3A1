def my_function(*args, **kwargs):
    toReturnList = []
    for arg in args:
        if type(arg) == dict:
            if any([True if type(key) == str and len(key) >= 3 else False
                    for key in arg.keys()]) and len(arg.keys()) >= 2:
                toReturnList.append(arg)

    for kw in kwargs.keys():
        if type(kwargs[kw]) == dict:
            if any([True if type(key) == str and len(key) >= 3 else False
                    for key in kwargs[kw].keys()]) and len(kwargs[kw].keys()) >= 2:
                toReturnList.append(kwargs[kw])

    return toReturnList


print(my_function(

    {1: 2, 3: 4, 5: 6},

    {'a': 5, 'b': 7, 'c': 'e'},

    {2: 3},

    [1, 2, 3],

    {'abc': 4, 'def': 5},

    3764,

    dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'},

    test={1: 1, 'test': True}

))
