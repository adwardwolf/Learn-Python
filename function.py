# A function is a block of cod that are used to perform a task

def hello(name):
    print("Hello", name)


def hello_full_name(first, last):
    print("Hello", first, last)


def print_me(name, age, height, country, city):
    print("Name:", name)
    print("Age:", str(age), "years old")
    print("Height:", str(height), "cm")
    print("Country:", country)
    print("City:", city)


nick_name = "adwardwo1f"
first_name = "So"
last_name = "Sovanrotha"
my_age = 19
my_height = 173.5
my_country = "Cambodia"
my_city = "Phnom Penh"

hello(nick_name)
hello_full_name(first_name, last_name)
print_me(nick_name, my_age, my_height, my_country, my_city)


# Keyword arguments

def print_name(first, middle, last):
    print(first, middle, last)


print_name(middle="Gustav", last="Jung", first="Carl")


# Return statement

def multiply(num1, num2):
    return num1 * num2


def plus(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def divide(num1, num2):
    return num1 / num2


multiply_result = multiply(8, 4)
plus_result = plus(8, 4)
subtract_result = subtract(8, 4)
divide_result = divide(8, 4)

print("8 * 4 is:", multiply_result)
print("8 + 4 is:", plus_result)
print("8 - 4 is:", subtract_result)
print("8 / 4 is:", int(divide_result))


# *args
# If you do not know how many arguments that will be passed into your function,
# add a * before the parameter name in the function definition.
# This way the function will receive a tuple of arguments.

def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


print(add(1, 2, 3, 4, 5, 6))


# **kwargs
# If you do not know how many keyword arguments that will be passed into your function,
# add two asterisk: ** before the parameter name in the function definition.
# This way the function will receive a dictionary of arguments

def hello_kwargs(**kwargs):
    print("Hello", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")


hello_kwargs(first="Carl", middle="Gustav", last="Jung")
