pos=-1
def linearSearch(lst,num):
    for i in range(0,len(lst)-1):
        if lst[i]==num:
            globals()['pos']=i
            return True
    return False

Record=[8,9,6,4,7,98,52,63,0,114,55,66,85,69,32]
element=int(input("Enter the number to search in the list:"))

if linearSearch(Record,element):
    print("Element is found at position:",pos+1)
else:
    print("Element is not found")
