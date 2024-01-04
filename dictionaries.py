stDetails = {}
stDetails["Name"] = "Geesad Bandara"
stDetails["Age"] = "20"
stDetails["Gender"] = "Male"
print(stDetails)

teacherDetails = {"Name":"Dulsha Nethsarani"}
print(teacherDetails)

print(stDetails["Name"])

del stDetails["Gender"]
print(stDetails)

#in a dictionary dict_name["key_name"]=key_value
for k in stDetails.keys():
    print("Got key",k,"maps to value",stDetails[k])

#dictionary methods
print("Key",stDetails.keys())
print("Value",stDetails.values())
print("Items",stDetails.items())

for k,v in stDetails.items():
    print(k,":" ,v)

l6 = list(stDetails)
print(l6)

l7 = list(stDetails.keys())
print(l7)
#so that way we can see that both of them giives the same output

l6 = list(stDetails.items())
print(l6)
#this creates a list of tuples
print(l6[0])
print(l6[0][1])

print("Geesad Bandara" in stDetails)
print("Name" in stDetails)
print("Name" in stDetails.keys())
print("Geesad Bandara" in stDetails.values())
print("Name: Geesad Bandara" in stDetails)
print("Name: Geesad Bandara" in stDetails.items())
print("('Name', 'Geesad Bandara')" in stDetails.items())

#get() method gets the the value of the key we have passed as the param

stock = {'apples': 430,
         'bananas': 312,
         'pears': 217}
print(stock.get("apples"))
print(stock.get("dell","Nope"))

#alising and copying
opposites = {"up": "down", "right": "wrong", "yes": "no"}
newOpposite = opposites
newOpposte2 = opposites.copy()
opposites["open"]= "close"
print(newOpposite)
print(newOpposte2)

updateOpposite = {"long":"short","close":"far"}
print(newOpposite)
print(opposites)
#dictionary methods
#adding a new iitems(not item items) to a dict
newOpposite.update(updateOpposite)
print(newOpposite)
#removing items
#this way we can remove item usin the key
reItem = updateOpposite.pop("long")
print(updateOpposite)
print(reItem)
reItem = updateOpposite.popitem()
print(reItem)
updateOpposite.update({"hi":"bye"})
print(updateOpposite)

#creating a dict without vales jst keys 
keys = ["name", "age", "city"]
my_dict = dict.fromkeys(keys, "Unknown")
print(my_dict)
my_dict["name"] = "Geesad Bandara"
print(my_dict)

#here we are in the best place to learn f strings :)

userAdmin = {"name":"Geesad Bandara","age":"20","gender":"male"}
print(f"{userAdmin['name']} is a boy and he is {userAdmin['age']}")

user = {'name': 'John Doe', 'occupation': 'gardener'}
print(f"{user['name']} is a {user['occupation']}")
