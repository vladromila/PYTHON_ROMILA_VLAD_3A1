def validateLists(rules, d):

    for (key, value) in d.items():
        isInRules = False
        for rule in rules:
            if rule[0] == key:
                isInRules = True
        if isInRules == False:
            return False

    for (key, value) in d.items():
        for rule in rules:
            if rule[0] == key:
                if not value.startswith(rule[1]):
                    return False
                if rule[2] not in value:
                    return False
                if not value.endswith(rule[3]):
                    return False

    return True


print(validateLists({("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}, {
    "key1": "come inside, it's too cold out", "key2": "start test middle in the winter"}))
