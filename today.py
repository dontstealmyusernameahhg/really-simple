print ("eenter the mraks in five sudjects")

markOne = int(input("first subject *burp*: "))
markTwo = int(input("second subject *burp*: "))
markThree = int(input("third subject *burp*: "))
markFour = int(input("fourth subject *burp*: "))
markFive = int(input("fifth subject *burp*: "))
total = markOne + markTwo + markThree + markFour + markFive
averagerge = total / 5
if averagerge >= 91 and averagerge <= 100:
    print("grade A+")
elif averagerge >= 81 and averagerge <= 91:
    print("grade A")
elif averagerge >= 71 and averagerge <= 81:
    print("grade B+")
elif averagerge >= 61 and averagerge <= 71:
    print("grade B")
elif averagerge >= 51 and averagerge <= 61:
    print("grade C+")
elif averagerge >= 41 and averagerge <= 51:
    print("grade C")
elif averagerge >= 31 and averagerge <= 41:
    print("grade D+")
elif averagerge >= 21 and averagerge <= 31:
    print("grade D")
elif averagerge >= 0 and averagerge <= 21:
    print("grade F-")
else:
    print("INVALID *burp* u r poo poo")