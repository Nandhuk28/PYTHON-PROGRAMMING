#Lowercase to Uppercase and Vice Versa
ch = input("Enter a character: ")

if 'A' <= ch <= 'Z':
    print(ch.lower())
else:
    if 'a' <= ch <= 'z':
        print(ch.upper())
    else:
        if '0' <= ch <= '9':
            print(0)
        else:
            print('*')
'''----------------------------------------------------------------------------------------'''

temp = int(input("Enter temperature: "))

if temp < 0:
    print("Freezing Weather")
else:
    if temp < 10:
        print("Very Cold Weather")
    else:
        if temp < 20:
            print("Cold Weather")
        else:
            if temp < 30:
                print("Normal Temperature")
            else:
                if temp < 40:
                    print("Hot")
                else:
                    print("Very Hot")
'''-------------------------------------------------------------------------------------'''
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

if a > b:
    if a > c:
        if a > d:
            print(a, "is largest")
        else:
            print(d, "is largest")
    else:
        if c > d:
            print(c, "is largest")
        else:
            print(d, "is largest")
else:
    if b > c:
        if b > d:
            print(b, "is largest")
        else:
            print(d, "is largest")
    else:
        if c > d:
            print(c, "is largest")
        else:
            print(d, "is largest")
'''---------------------------------------------------------------------------------'''


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b:
    if a > c:
        print(a, "is largest")
    else:
        print(c, "is largest")
else:
    if b > c:
        print(b, "is largest")
    else:
        print(c, "is largest")

'''---------------------------------------------------------------------------------'''

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter operator: ")

if op == '+':
    print(a + b)
else:
    if op == '-':
        print(a - b)
    else:
        if op == '*':
            print(a * b)
        else:
            if op == '/':
                print(a / b)
            else:
                if op == '%':
                    print(a % b)
                else:
                    if op == '//':
                        print(a // b)
                    else:
                        if op == '**':
                            print(a ** b)
                        else:
                            print("Invalid Operator")
'''------------------------------------------------------------------------------'''


day = int(input("Enter day number: "))

if day == 1:
    print("Sunday")
else:
    if day == 2:
        print("Monday")
    else:
        if day == 3:
            print("Tuesday")
        else:
            if day == 4:
                print("Wednesday")
            else:
                if day == 5:
                    print("Thursday")
                else:
                    if day == 6:
                        print("Friday")
                    else:
                        if day == 7:
                            print("Saturday")
                        else:
                            print("Invalid Day")
'''--------------------------------------------------------------------------------------------------------'''

ch = input("Enter a character: ")

if 'A' <= ch <= 'Z' or 'a' <= ch <= 'z':
    print("Alphabet")
else:
    if '0' <= ch <= '9':
        print("Digit")
    else:
        print("Special Character")
