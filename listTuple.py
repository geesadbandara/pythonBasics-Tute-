#created a list
l = []
#added items to a null list
l.append("Name: Geesad")
l.append("Age: 20")
print(l)

l.insert(2,"Address: Park Lane,London")
print(l)
#lets try whether we can use insert something into to be created indexing
l.insert(4,"School : D.S Senanayake College, Colombo 7.")
#nope it always add to the last index
print(l[3])
l.insert(3,"University: IIT")
print(l)

#so what if we want to add more than one element to the list

l.extend(["Preference: Non-Veg", "Gender: Male"])
print(l)

#but we haven't added data above append,simply extends() is like extending list
#using another list
l.pop(5)
print(l)

l.remove("Gender: Male")
print(l)

l2 = l.copy()
print("l2",l2)

l3 = l
print("copy of l1",l)
l.clear()
print(l)
print(l2)
print(l3)

#so but think what happen if we create dataset we can edit but it have to be a data
#which can't be change so that's where tuple comes in
#list into tuples
t = tuple(l2)
print(t)
#think we need to add something to a tuple that means do we need to convert tuple into
#into list do the stuf and add?
l4 = list(t)
l4.append("Gender: Male")
t2 = tuple(l4)
print(l4)
print(t2)

#traversing the the list and tuple
#list

print("Name: Geesad","Name: Geesad" in l2)
print("Name: Banula","Name: Banula" in l2)
#list indexing
print("Index of Name:Geesad", l2.index("Name: Geesad"))
#tuple
print("Name: Geesad","Name: Geesad" in t2)
#tuple indexing
print("Index of Name:Geesad", t2.index("Name: Geesad"))

#listSlciing
temp = [18, 21, 24, 33, 39, 40, 39, 36, 30, 22, 18]
print(temp[6:9])
print(temp[6:])
print(temp[6])
print(temp[:6])

#print the square of the nmbers are higher than 2
numbers = [4, 2, 3, 1, 5]
square = []
for num in numbers:
    if (num>2):
        squareVal = num**2
        square.append(squareVal)
        continue
print(square)

#lets simplyfy it using the list comprehensions
squares = [number**2 for number in numbers if number > 2]
print(squares)
