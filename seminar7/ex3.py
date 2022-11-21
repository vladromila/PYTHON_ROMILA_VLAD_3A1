import re


def get_strings(reglist, stringlist):
    toReturnStrings = []
    for string in stringlist:
        matchedCases = 0
        for reg in reglist:
            if re.match(reg, string):
                matchedCases = matchedCases+1
        if matchedCases > 0:
            toReturnStrings.append(string)
    return toReturnStrings
