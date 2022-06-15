from unicodedata import digit

# num2 = input("Enter num2: ")
# operator = input("Select operation (+,-,%, //, *, **: )")

while True:
    num1 = input("Enter num1: \n")
    if not (num1 is digit()):
        print("Not a number!")
        break
    else:
        num1 = int(num1)
        if num1 % 2 == 0 and num1 < 100:
            print("Valid")
        else:
            print("Try again!")
            continue
