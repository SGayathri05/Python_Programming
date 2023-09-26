from math import *
from collections import *
from sys import *
from os import *

def lengthOfLongestConsecutiveSequence(arr, n):
    # Write your code here.
    count = 1
    ans = count
    arr.sort()
    maxi = 0
    for i in range(n-1):
        if arr[i]+1==(arr[i+1]):
            count+=1
            ans = max(ans, count)
        elif arr[i]==(arr[i+1]):
            continue  
        else:
            count=1
    return ans    

