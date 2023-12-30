
#sentenceEditor
newWord = ""
print("Menue \n 1)UpperCase \n 2)LowerCase \n 3)Find a certain word")
userIn = int(input("Enter your preferences: "))
if(userIn == 1):
    userStr = input("Enter the word or sentence: ")
    for x in userStr:
        newWord =newWord + x.upper()
    print(newWord)
elif(userIn == 2):
    userStr = input("Enter the word or sentence: ")
    for x in userStr:
        newWord =newWord + x.lower()
    print(newWord)
elif(userIn == 3):
    userStr = input("Enter the word or sentence")
    searchFor = input("Enter the word you wanna search: ")
    if(searchFor in userStr):
        print("There is that word")
    else:
        print("There is no such word")
else:
    print("Can't understand the selection: ")
    
    
