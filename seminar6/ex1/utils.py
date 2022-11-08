def process_item(x):
    x += 1
    hasFoundNextPrimeNumber = False
    while hasFoundNextPrimeNumber == False:
        hasFoundDivider = False
        for nr in range(2, int(x**(1/2)) + 1):
            if x % nr == 0:
                hasFoundDivider = True
                x += 1
                break
        if hasFoundDivider == False:
            hasFoundNextPrimeNumber = True
    return x


def main():
    x = int(input("Enter your number:"))
    print(process_item(x))


if __name__ == '__main__':
    main()
