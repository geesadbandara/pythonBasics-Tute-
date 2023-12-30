import random

count = 0
doubleCount = 0
while(count<10):
    die1 = random.randint(1,7)
    #print(die1)
    die2 = random.randint(1,7)
    #print(die2)
    count = count + 1
    if(die1 == die2):
        doubleCount = doubleCount + 1
        
        
        continue

print(doubleCount)
