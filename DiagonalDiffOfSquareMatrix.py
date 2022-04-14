def diagonalDifference(arr):
    d1sum=0
    d2sum=0
    for i in range(0,len(arr)):
        d1sum=d1sum+arr[i][i]
        
    for r in range(0,len(arr)):
        d2sum=d2sum+arr[r][len(arr)-1-r]
    return abs(d1sum-d2sum)


arr1=[[11,2,4],[4,5,6],[10,8,-12]]
print("Unique Value in array:",diagonalDifference(arr1))
