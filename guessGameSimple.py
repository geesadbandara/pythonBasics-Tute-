import random
secret_num = random.randint(1,20)

userNum =  int(input("Enter a number between 1 - 20 :"))

if(secret_num == userNum):
    print("Guess is correct")
else:
    print("Guess is wrong")
    print("Secret Number is ",secret_num)
