from math import *
from collections import *
from sys import *
from os import *




def rotateMatrix(mat, n, m):

    # Write your code here
    l,r,t,b=0,m-1,0,n-1
    while (t<b and l<r):
        temp=mat[t][l]
        for i in range(l+1,r+1):
            temp,mat[t][i]=mat[t][i],temp
        t+=1
        for i in range(t,b+1):
            temp,mat[i][r]=mat[i][r],temp
        r-=1
        for i in range(r,l-1,-1):
            temp,mat[b][i]=mat[b][i],temp
        b-=1
        for i in range(b,t-1,-1):
            temp,mat[i][l]=mat[i][l],temp

        l=l+1
        mat[t-1][l-1]=temp
       
    
    return mat
    pass
    
    
