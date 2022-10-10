def mostCommonLetter():
    sentence = input("Enter your sentence: ")
    max = 1
    for l in sentence:
        numberOfAppearances = sentence.count(l)
        if numberOfAppearances > max:
            max = numberOfAppearances
            letter = l
    print(letter)
