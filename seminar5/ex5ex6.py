import os


def fileContainsSearchedString(target, to_search):
    f = open(target, "rt")
    text = f.read()
    f.close()
    return to_search in text


def checkFileOrDir(target, to_search):
    if (os.path.isfile(target)):
        if fileContainsSearchedString(target, to_search):
            return [target]
        else:
            return []
    elif (os.path.isdir(target)):
        toReturnFiles = []
        for r, d, files in os.walk(target):
            for f in files:
                name = os.path.join(r, f)
                if fileContainsSearchedString(name, to_search):
                    toReturnFiles += [name]
        return toReturnFiles
    else:
        raise ValueError("Target path is not a file or dir")


print(checkFileOrDir("./testfolder", "asdasdasd"))


def functWithErrorCallback(target, to_search, cb):
    try:
        return checkFileOrDir(target, to_search)
    except Exception as e:
        cb(e)
        return []
