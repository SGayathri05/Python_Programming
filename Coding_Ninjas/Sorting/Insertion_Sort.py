from typing import List

def insertionSort(a: List[int], n: int) -> None:
   # write your code here
   res = []
   # n = len(a)
   for i in range(1, n):
      cur_ele = a[i]
      pos = i
      while cur_ele<a[pos-1] and pos>0:
         a[pos] = a[pos-1]
         pos= pos-1
      a[pos] = cur_ele
      res.append(a)
   return res
 
       
