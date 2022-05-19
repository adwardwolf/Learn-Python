name = "Sovanrotha"

print("My name is", name)
print("The length of my name is", len(name))
print("The index of letter \"n\" in my name is", name.find("n"))
print("My name after capitalized is", name.capitalize())
print("My name in uppercase is", name.upper())
print("My name in lowercase is", name.lower())
print("Number of letters \"o\" in my name is", name.count("o"))
print("My name after replaced \"o\" with \"i\"", name.replace("o", "i"))

# str.format()

animal = "racoon"
item = "moon"

print("The {} jumped over the {}".format(animal, item))
print("The {1} jumped over the {0}".format(item, animal))  # positional argument
print("The {animal} jumped over the {item}".format(item=item, animal=animal))  # keyword argument

text = "The {} jumped over the {}"
print(text.format(animal, item))

pi = 3.14159
one_thousand = 1000

print(pi, "is {:.3f}".format(pi))
print(str(one_thousand), "is {:,}".format(one_thousand))  # add comma after 3 digits
print("Binary num of", str(one_thousand), "is {:b}".format(one_thousand))  # convert num to binary
print("Octal num of", str(one_thousand), "is {:o}".format(one_thousand))  # convert num to octal
print("Hexadecimal num of", str(one_thousand), "is {:x}".format(one_thousand))  # convert num to hexadecimal
print(str(one_thousand), "is equal {:e}".format(one_thousand))
