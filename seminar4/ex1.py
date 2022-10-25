def operations(a, b):
    return [set(a+b), set(set(a) & set(b)), set(set(a)-set(b)), set(set(b)-set(a))]


print(operations([1, 2, 3, 4], [3, 4, 5, 6]))
