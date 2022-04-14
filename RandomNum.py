#Python program to print random number
import random
def RandInt():
    print("Enter 'T' to generate a random number")
    opt=input("Enter option: ")
    if opt=='T':
        print(">",random.randint(0,9))
RandInt()
