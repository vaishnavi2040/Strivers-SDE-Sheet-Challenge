from os import *
from sys import *
from collections import *
from math import *

def nextPermutation(per, n):
    # Write your code here.
    # Return a list.
    pivot=0
    
    for i in range(n-1,0,-1):
        if per[i-1]<per[i]:
            pivot=i
            break
    if pivot == 0:
        per.sort()
        return per
    swap=n-1
    
    while per[pivot-1]>=per[swap]:
        swap-=1
        
    per[swap],per[pivot-1]=per[pivot-1],per[swap]
    
    per[pivot:]=sorted(per[pivot:])
    return per
