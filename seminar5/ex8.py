import os


def getFilePaths(directory):
    try:
        toReturnPaths = []
        files = [f for f in os.listdir(directory)]
        for f in files:
            toReturnPaths.append(os.path.abspath(os.path.join(directory, f)))
        return toReturnPaths
    except Exception as e:
        return str(e)


print(getFilePaths("/Users/vladromila/Desktop/facultate/PYTHON/testfolder"))
