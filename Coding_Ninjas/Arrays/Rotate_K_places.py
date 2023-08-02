from os import *
from sys import *
from collections import *
from math import *

#Your code goes here.
n = int(input())
arr = list(map(int, input().split()))
k = int(input())

res = arr[k:]+arr[:k]
for i in res:
    print(i, end=" ")
