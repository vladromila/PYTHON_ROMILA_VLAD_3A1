import os


def checkPath(my_path):
    if os.path.isdir(my_path):
        toReturnList = {}
        for r, d, files in os.walk(my_path):
            for file in files:
                extension = file.split(".")[len(file.split("."))-1]
                if extension in toReturnList:
                    toReturnList[extension] += 1
                else:
                    toReturnList[extension] = 1

        return sorted(toReturnList.items(), key=lambda el: el[1], reverse=True)
    elif os.path.isfile(my_path):

        f = open(my_path, "rb")
        fileSize = os.path.getsize(my_path)
        if fileSize < 20:
            raise Exception(
                "The file content does not respect the minimum length of 20 characters")
        f.seek(fileSize-20)
        return f.read()
    else:
        raise Exception("Invalid path.")


print(checkPath("./testfolder/test.txt"))
