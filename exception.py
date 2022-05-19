
try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
except ZeroDivisionError as e:
    print("Exception:", e)
    print("You can't divide by zero!")
except ValueError as e:
    print("Exception:", e)
    print("Please enter only numbers!")
except Exception as e:
    print("Exception:", e)
    print("Something went wrong :(")
else:
    print("Result:", result)
finally:
    print("This will always execute")
