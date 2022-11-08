def multipleMethods(s):

    def normalFunctionThatMapsStr(s):

        return [c for c in s if c.lower() in "aeiou"]

    def aFunction(s): return [
        c for c in s if c.lower() in "aeiou"]

    list1 = normalFunctionThatMapsStr(s)

    list2 = aFunction(s)

    def lambdaFilter(s): return list(
        filter(lambda c: c.lower() in "aeiou", s))

    list3 = lambdaFilter(s)

    return list1, list2, list3


print(multipleMethods("Programming in Python is fun"))
