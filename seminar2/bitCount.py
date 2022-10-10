def bitCount():
    number = int(input("Enter the number: "))
    # print(number.bit_count())
    # # lazy
    binStr = bin(number).split("0b")[1]
    print(binStr.count("1"))
