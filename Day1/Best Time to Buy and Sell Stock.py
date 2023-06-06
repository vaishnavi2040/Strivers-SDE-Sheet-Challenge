from os import *
from sys import *
from collections import *
from math import *
import sys as sys

def maximumProfit(prices):
    # Write your code here.
    ma=-sys.maxsize-1
    mi=sys.maxsize
    for i in range(len(prices)):
        mi=min(mi,prices[i])
        ma=max(ma,prices[i]-mi)
    return ma
