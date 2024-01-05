#timestable
multi = 0
def timestable(num):
    for x in range(1,13):
        multi = num*x
        print(multi)
userIn = int(input("Enter the table you want :"))  
timestable(userIn)
