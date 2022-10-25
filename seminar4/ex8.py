def getPath(mapping):
    if "start" not in mapping:
        return []
    else:
        currentKey = mapping["start"]
        toReturnList = []
        usedKeys = set()
        while currentKey not in usedKeys:
            toReturnList.append(currentKey)
            usedKeys.add(currentKey)
            currentKey = mapping[currentKey]
        return toReturnList


print(getPath({'start': 'a', 'b': 'a', 'a': '6', '6': 'z',
      'x': '2', 'z': '2', '2': '2', 'y': 'start'}))
