from classes.car import Car

chevy = Car("Chevy", "Corvette", 2021, "blue")
mustang = Car("Ford", "Mustang", 2022, "black")

print(chevy.make)
print(chevy.model)
print(chevy.year)
print(chevy.color)
chevy.drive()
chevy.stop()

print(mustang.make)
print(mustang.model)
print(mustang.year)
print(mustang.color)
mustang.drive()
mustang.stop()
