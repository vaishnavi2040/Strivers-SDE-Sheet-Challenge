from os import *
from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit

class Solution:
    def __init__ (self, start, end):
        self.start = start
        self.end = end

def mergeIntervals(arr):
    # s=intervals[0]
    # e=intervals[0]
    # print(s)
    # k=0
    # arr=[]
    # for i in range(len(s)):
    #     arr[i]=[s[i],e[i]]
        
    arr=sorted(arr,key= lambda i:i.start)
    ans=[]
    ans.append(arr[0])
    j=0
    
    for i in range(len(arr)):
        
        if arr[i].start<=ans[j].end:
            ans[j].end=max(ans[j].end,arr[i].end)
        else:
            ans.append(arr[i])
            j+=1
            
    return ans
    pass
    

n = int(input())
arr1 = list(map(int, stdin.readline().strip().split(" ")))
arr2 = list(map(int, stdin.readline().strip().split(" ")))
arr1.sort()
arr2.sort()
intervals = []
for i in range(n):
    a = Solution(arr1[i], arr2[i])
    
    intervals.append(a)
    # print(intervals)

res = mergeIntervals(intervals)

for i in range(len(res)):
    print(res[i].start, res[i].end)
