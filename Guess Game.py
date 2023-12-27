#guess game
import random


def easy():
    secret_num = random.randint(1,20)
    while(True):
        userNum =  int(input("Enter a number between 1 - 20 :"))
        if(secret_num == userNum):
            print("Guess is correct")
            break
        else:
            print("Guess is wrong")
            if(secret_num < userNum):
                print("Try a lower number")
            else:
                print("Try a higher number")
            continue
def inter():
    secret_num = random.randint(1,20)
    while(True):
        userNum =  int(input("Enter a number between 1 - 20 :"))
        if(secret_num == userNum):
            print("Guess is correct")
            break
        else:
            print("Guess is wrong")
            
def hard():
    secret_num = random.randint(1,20)
    count = 0
    while(count < 10):
        userNum =  int(input("Enter a number between 1 - 20 :"))

        print("Chance: ", count)
        count= count + 1
        
        if(secret_num == userNum):
            print("Guess is correct")
            break
        else:
            print("Guess is wrong")
            if(secret_num < userNum):
                print("Try a lower number")
            else:
                print("Try a higher number")
            continue

def ins():
    state = True 
    while(state == True):
        try:
            print("-"*100)
            print("Welcome to guess game 1.0")
            print("Select \n1.Easy \n This mode you will be having unlimited chances with clues")
            print("2.Intermediate \n This mode you will have unlmited chances but no clues")
            print("3.Hard \n This mode you will have 10 chances to guess without any clues")
            print("4.Quit Game")

            mode = int(input("Select the mode : "))
            if(mode == 1):
                #easy
                print("Easy")
                easy()
            elif(mode == 2):
                #inter
                print("int")
                inter()
            elif(mode == 3):
                #hard
                print("hard")
                hard()
            elif(mode == 4):
                #quuiit
                break
            else:
                print("There is no such mode like that")


        except ValueError:
            print("Error")


ins()
