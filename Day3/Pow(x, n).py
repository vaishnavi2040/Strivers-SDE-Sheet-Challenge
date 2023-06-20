from math import *
from collections import *
from sys import *
from os import *

import sys
sys.setrecursionlimit(10**7)

def modularExponentiation(x, n, m):
	# Write your code here.
	if n==0:
		return 1
	if n<0:
		x=1/x
		n*=-1
		
	ans=modularExponentiation(x,n//2,m)
	return  (ans*ans if n%2==0 else x*ans*ans)%m


# Main.
t = int(input())
while (t > 0):
	lst = list(map(int,input().split()))
	x,n,m = lst[0], lst[1], lst[2]
	print(modularExponentiation(x, n, m))
	t -= 1
