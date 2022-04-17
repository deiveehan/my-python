thisset = {"apple", "banana", "cherry"}
print(thisset)

for ft in thisset:
    print(ft)


# Check if cherry is in this set
print("cherry" in thisset)
print("grapes" in thisset)

# Adding a new item to the set
thisset.add("Orange")
print("Orange" in thisset)

#Add multiple items to a set
thisset.update(["Guava", "Papaya", "Kiwi"])
print(thisset)
print(len(thisset))

# Remove an item
thisset.remove("banana")
print(thisset)
