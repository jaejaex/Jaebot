
num = ""
while num != "exit":
    num = input("Enter a number: ")
    if num == "":
        continue
    try:
        num = int(num)
    except:
        print("Not a number")
        continue
    if num == 8:
        print("Got 8")
    elif num == 9:
        print("Got 9")
    elif num > 10:
        print("That is too high")
    else:
        print("That is not a number")