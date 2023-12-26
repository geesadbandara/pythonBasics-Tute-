#heat convertor
print("Menue \n 1. Celsius to Fahrenheit \n 2. Fahrenheit to Celsius" )

try:
    response = int(input("Select a number from above:"))
    if(response == 1):
       f = float(input("Enter the Fahrenheit value:")) 
       c = (f - 32) / 1.8
       print("Celsius: ",c)

    elif(response == 2):
        c = float(input("Enter the Celsius value:"))
        f = (c * 1.8) + 32
        print("Fahrenheit: ",f)
    else:
        print("Can't recognize the Command")
except ValueError:
    print("You have to enter a integer")
