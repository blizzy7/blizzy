secret_number = 1000
while True:
    user = int(input("guess number "))
    if user ==secret_number:
        print("right")
        break
    else:
        print("try again")
        