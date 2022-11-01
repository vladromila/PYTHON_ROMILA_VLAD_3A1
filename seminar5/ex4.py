import os
import sys


def uniqueExtensions():
    try:
        assert (len(sys.argv) > 1), "Invalid arg"
        return sorted(list(set([f.split(".")[len(f.split("."))-1]
                                for f in os.listdir(sys.argv[1])
                                if os.path.isfile(os.path.join(sys.argv[1], f))
                                and os.path.splitext(f)[1] != ""])))
    except Exception as e:
        print(str(e))
        return []


print(uniqueExtensions())
