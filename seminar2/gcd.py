def gcd(a, b):
    if a<0 : 
        a = -a
    if b<0:
        b = -b
    while b!=0:
        a %= b
        if( a==0 ):
             return b
        b %= a
        
    return a

def runGCD():
    a=-1
    elements=[]
    while a!=0:
        a=int(input("Enter a value: "))
        if a!=0:
            elements.append(a)
    if len(elements)>=2:
        currentResult = gcd(elements[0], elements[1])
        for i in range(2, len(elements)):
            currentResult = gcd(currentResult, elements[i])
        print("The greatest common divisor is:",currentResult)
    else:
        if len(elements)==1:
            print("The greatest common divisor is:", elements[0])
        else:
            print("No elements have been added")
 

