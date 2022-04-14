import array

def lonelyinteger(a):
    for i in range(0,len(a)):
        if a.count(a[i])==1:
            b=a[i]
        else:
            pass
    return b

arr1=array.array("i",[1,2,3,2,1])
print("Unique Value in array:",lonelyinteger(arr1))
