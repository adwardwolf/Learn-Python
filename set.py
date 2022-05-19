# set = collection which is unordered, unindexed, and no duplicate values

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

sameElements = dishes.intersection(utensils)
diffElements = dishes.difference(utensils)

print("The same elements:", sameElements)
print("The different elements:", diffElements)

for x in dishes:
    print(x)
