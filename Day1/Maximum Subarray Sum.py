from os import *
from sys import *
from collections import *
from math import *
import sys as sys

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def maxSubarraySum(arr, n) :

	# Your code here
    # return the answer
    m=-sys.maxsize - 1
    sum=0
    for i in range(n):
        sum=sum+arr[i]
        if sum<0:
            sum=0
        m=max(m,sum)
        
    return m





















def takeInput() :
	
    n =  int(input())

    if(n == 0) :
        return list(), n

    arr = list(map(int, stdin.readline().strip().split(" ")))

    return arr, n


#main
arr, n = takeInput()
print(maxSubarraySum(arr, n))
