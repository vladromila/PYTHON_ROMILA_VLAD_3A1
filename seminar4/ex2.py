def letterCounter(string):
    dict = {}
    for char in string:
        dict[char] = dict.get(char, 0) + 1
    return dict


print(letterCounter("Ana has apples."))
