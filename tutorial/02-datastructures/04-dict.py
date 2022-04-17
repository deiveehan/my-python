thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}

print(thisdict)

x = thisdict["model"]
print("Model : " + x)
x = thisdict.get("model")
print("Model : " + x)

# Change the value
thisdict["year"] = 2018
print(thisdict)

# Loop through dict
for x in thisdict:
    print(x)

# Check if key exists
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")

# Length
print(len(thisdict))

# Add an attribute to the dictionary
thisdict["color"] = "red"
print(thisdict)

#Remove an item from the dictionary
thisdict.pop("model")
print(thisdict)

#Copy a dictionary
mydict = thisdict.copy()
print(mydict)

#Clear the dictionary
mydict.clear()
print(mydict)

#Creating using a constructor
thisdict = dict(brand="Ford", model="Mustang", year=1964)
print(thisdict)

#Nested dictionary
myfamily = {
    "child1" : {
        "name" : "Keerthi",
        "year" : 2008
    },
    "child2" : {
        "name" : "Pranavi",
        "year" : 2019
    }
}
print(myfamily)
