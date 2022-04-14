
try:
    a=int(input("Enter an integer value:"))
except ValueError:
    print("Hey!!, You didn't enter an integer value")
finally:
    print("The End!!")
