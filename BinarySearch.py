pos=-1
def BinarySearch(lst,num): 
    lb=0 #lower bound
    ub=len(lst)-1 #upper bound
    while lb<=ub:
        mid=(lb+ub)//2
        if lst[mid]==num:
            globals()['pos']=mid
            return True
        else:
            if lst[mid]<num:
                lb=mid+1
            else:
                ub=mid-1
    return False

Record=[8,9,6,4,7,98,52,63,0,114,55,66,85,69,32]
Record.sort()
element=int(input("Enter the number to search in the list:"))
print("Sorted List is:",Record)
if BinarySearch(Record,element):
    print("Element is found at position:",pos+1)
else:
    print("Element is not found")
