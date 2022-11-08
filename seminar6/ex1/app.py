import utils


def main():
    while True:
        x = input("Enter your number: ")
        if x == "q":
            return
        try:
            x = int(x)
        except Exception as e:
            print("Wrong number. Please enter a valid integer.")
        else:
            print(utils.process_item(x))


if __name__ == '__main__':
    main()
