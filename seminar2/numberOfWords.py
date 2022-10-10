def numberOfWords():
    str = input("Enter your sentence: ")
    str = ' '.join(str.split())

    print(len(str.split(" ")))
