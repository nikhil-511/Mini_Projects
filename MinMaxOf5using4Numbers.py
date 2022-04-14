#Python program to add two integers
import numpy
def miniMaxSum(arr):
    tot = numpy.sum(arr)
    mx = numpy.max(arr)
    mn = numpy.min(arr) 
    print(tot-mx,"  ",tot-mn)

a = numpy.array([1, 2, 3, 4, 5])
miniMaxSum(a)
