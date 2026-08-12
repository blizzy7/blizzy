def largest_number(num1 , num2, num3):
    if num1 >= num2 and num1 >= num3:
        print(f"{num1} is the largest")
    elif num2 >= num1 and num2 >= num3:
        print(f"{num2} is the largest")
    else:
        print(f"{num3} is the largest ")
largest_number(10,3,16)
