from typing import List

def commonPrefix(arr: List[str], n: int) -> str:
    # Write your code here
    res = arr[0]
    n = len(res)
 
   
    for i in range(1, len(arr)):
       
        while arr[i].find(res) != 0:
            
            res = res[:n- 1]
            n -= 1
 
           
            if not res:
                return "-1"
 
    return res
