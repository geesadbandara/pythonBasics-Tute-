f = open("shopping.txt", "w" )
f.close()
def UserInput():
    userString = input("Enter a word: ")
    f = open("shopping.txt", "a" )
    f.write(userString+"\n")
    f.close()

def calc(item,quantity,price):
    totalPrice = quantity*price
    print("Item ",item, "=", totalPrice )

def readFile():
    f = open("shopping.txt", "r")
    for line in f:
        word = line.split()
        item = word[0]
        quantity = int(word[1])
        price = float(word[2])
        calc(item,quantity,price)
    f.close()
    

count = 0    
while(count<3):
    UserInput()
    
    count = count + 1
    
readFile()
