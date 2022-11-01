import os


def getFileExtensions(directory):
    try:
        extensions = set()
        files = [f for f in os.listdir(directory) if os.path.isfile(
            os.path.join(directory, f))]
        for f in files:
            extensions.add(f.split(".")[len(f.split("."))-1])
        toReturnList = list(extensions)
        toReturnList.sort()
        return toReturnList
    except Exception as e:
        return str(e)


print(getFileExtensions("/Users/vladromila/Desktop/facultate/PYTHON/testfolder"))
