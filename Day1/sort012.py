from os import *
from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def sort012(arr, n) :

	# write your code here
    # don't return anything 
    i=0
    k=0
    j=n-1
    while(k<=j):
        if arr[k]==0:
            arr[k],arr[i]=arr[i],arr[k]
            i=i+1
            k=k+1
        elif arr[k]==2:
            arr[k],arr[j]=arr[j],arr[k]
            j=j-1
            
        else:
            k=k+1
    


#taking inpit using fast I/O
def takeInput() :
	n = int(input().strip())

	if n == 0 :
		return list(), 0

	arr = list(map(int, stdin.readline().strip().split(" ")))

	return arr, n



def printAnswer(arr, n) :
    
    for i in range(n) :
        
        print(arr[i],end=" ")
        
    print()
    
#main

t = int(input().strip())
for i in range(t) :

    arr, n= takeInput()
    sort012(arr, n)
    printAnswer(arr, n)
