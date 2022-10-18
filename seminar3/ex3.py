def listFunctions(list1, list2):
    return [list1+list2, list(set(list1) & set(list2)), list(set(list1)-set(list2)), list(set(list2)-set(list1))]


list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
print(listFunctions(list1, list2))
