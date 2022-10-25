def dictionariesEquels(d1, d2):
    for i in d1:
        if d1[i] not in d2.values() or i not in d2:
            return False

    for item in d2:
        if d2[item] not in d1.values() or item not in d1:
            return False

    return True
