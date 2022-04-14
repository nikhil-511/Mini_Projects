
def SelectionSort(lt):
    lst=lt
    for i in range(len(lst)-1):
        minval=i
        for j in range(i,len(lst)):
            if lst[j]<lst[minval]:
                minval=j
        lst[i],lst[minval]=lst[minval],lst[i]
    return lst

    
Record=[8,9,6,4,95,6,3,963,559,1496,630,8,1,0]
print("UnSorted List is:",Record)
SortedRecord=SelectionSort(Record)
print("Sorted List is:",SortedRecord)
