def numberOfVowels():
    vowelsCounter=0

    toVerifyString=input("Your string: ")
    vowels="aeiou"
    for character in toVerifyString:
        if vowels.find(character)>=0:
            vowelsCounter+=1
    print(vowelsCounter)