
def calc_ulator():

    num1=int(input("Enter 'A' as your 1st no. \n"))
    num2=int(input("Enter 'B' as your 2nd no. \n"))
    print('So,What do you want? + , - , * , / , ** . \n Other options will be coming soon.')
    num=input()
    if num=='+':
        Result=num1+num2
        print(Result)
    elif num=='-':
        Result=num1-num2
        print(Result)
    elif num=='*':
        Result=num1*num2
        print(Result)
    elif num=='/':
        Result=num1/num2
        print(Result)
    elif num=='**':
        Result=num1**num2
        print(Result)
    else:
        print("Error! Please check your input. \n Other options will be available soon.")
    
    if input("Calculate again? (y/n): ").lower() == "y":
        print(calc_ulator())
    else:
        print("Please be back for more calculations...")

print(calc_ulator())

