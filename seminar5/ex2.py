import os


def generateFile(directory, file):
    try:
        f = open(file, "w")

        files = [f for f in os.listdir(directory) if os.path.isfile(
            os.path.join(directory, f))]
        for fl in files:
            if fl.lower().startswith("a"):
                f.write(fl+"\n")

        f.close()
    except Exception as e:
        return str(e)


generateFile("/Users/vladromila/Desktop/facultate/PYTHON/testfolder/",
             "/Users/vladromila/Desktop/facultate/PYTHON/testfolder/result.res")
