
def BubbleSort(lst):
    lst1=lst
    for i in range(len(lst1)-1,0,-1):
        for j in range(i):
            if lst1[j]>lst1[j+1]:
                lst1[j],lst1[j+1]=lst1[j+1],lst1[j]
    return lst1

    
Record=[8,9,6,4,95,6,3,963,559,1496,630,8,1,0]
print("UnSorted List is:",Record)
SortedRecord=BubbleSort(Record)
print("Sorted List is:",SortedRecord)
