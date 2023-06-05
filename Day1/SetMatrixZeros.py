from math import *
from collections import *
from sys import *
from os import *

from typing import List

def setZeros(matrix: List[List[int]]) -> None:
	# Write your code here.
        n=len(matrix)
        m=len(matrix[0])
        
        col_00=False
        
        for i in range(0,n):
            if matrix[i][0]==0:
                col_00=True
            for j in range(1,m):
                if matrix[i][j]==0:
                    matrix[0][j]=0
                    matrix[i][0]=0
                    
        for i in range(1,n):
            for j in range(1,m):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
                    
        if matrix[0][0]==0:
            
            for j in range(0,m):
                matrix[0][j]=0
                
        if col_00==True:
            for i in range(0,n):
                matrix[i][0]=0
            

            
                
    
