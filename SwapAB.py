#Swapping A & B
def SwapAB():
    a=input("Enter A:")
    b=input("Enter B:")
    print("BEFORE SWAPPING: A={0} & B={1}".format(a,b))
    a,b=b,a
    print("AFTER SWAPPING: A={0} & B={1}".format(a,b))
SwapAB()
