import os
import re


def findFiles(path, reg):
    for dirpath, dirs, files in os.walk(path):
        for filename in files:
            if re.match(reg, filename) and len(re.findall(reg, filename)) > 0:
                print(">>"+filename)
            else:
                if re.match(reg, filename):
                    print(filename)
                else:
                    if len(re.findall(reg, filename)) > 0:
                        print(filename)


findFiles(".", r'\bex5\+')
