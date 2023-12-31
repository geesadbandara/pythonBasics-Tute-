#simple calculator
num1 = int(input("Enter number 1: "))
print("Menue of operators \n + \n - \n * \n /")
operator = input("Select a operator from above list: ")
num2 = int(input("Enter number 2: "))

if(operator == "+"):
    answer = num1 + num2
    print("Answer = ", answer)
elif(operator == "-"):
    answer = num1 - num2
    print("Answer = ", answer)
elif(operator == "*"):
    answer = num1*num2
    print("Answer = ", answer)
elif(operator == "/"):
    if(num2!=0):
        answer = num1/num2
        print("Answer = ", answer)
    else:
        print("Number 2 can't be 0 ")
else:
    print("Wrong Operator")
