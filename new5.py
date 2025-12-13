stop = True

while stop:
    num = int(input("please choose number 1,2,3"))
    if (num == 1):
        print("Your number is one")
    elif (num == 2):
        print("Your number is two")
    elif (num == 3):
        print("Your number is three")
    elif (num == 4):
        print("Your number is Thank you for using our programe")
        stop = False
    else:
        print("Please choice number only or 1,2,3,4")