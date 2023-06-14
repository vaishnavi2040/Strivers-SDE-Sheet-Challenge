from math import *
from collections import *
from sys import *
from os import *

def missingAndRepeating(arr, n):
    # Write your code here
    s=n*(n+1)/2
    square_sum=(n*(n+1)*(2*n+1))/6
    s1=0
    s2=0
    for i in range(n):
        s1=s1+arr[i]
        s2=s2+arr[i]*arr[i]

    x=s-s1
    y=square_sum-s2
    t=y/x
    miss=(x+t)/2
    rep=(t-x)/2
    return int(miss),int(rep)
    
        
 
