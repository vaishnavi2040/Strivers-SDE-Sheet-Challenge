from os import *
from sys import *
from collections import *
from math import *

def getInversions(arr, n) :
	# Write your code here. 
    count=0
    for i in range(n):
        for j in range(i,n):
            if arr[i]>arr[j]:
                count+=1
    return counta

# Taking inpit using fast I/O.
def takeInput() :
    n = int(input())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n

# Main.
arr, n = takeInput()
print(getInversions(arr, n))
