type = ""
def negativePositiveZero(number):
    if(number>0):
        type = "Postive"
    elif(number == 0):
        type = "Zero"
    else:
        type = "Negative"
    return type
number = float(input("Enter the number :"))
answer = negativePositiveZero(number)
print(f"Type of the entered value is : {answer}") 
