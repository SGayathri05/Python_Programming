def traffic(n: int, m: int, vehicle: [int]) -> int:
    # Write your code here.
    left = 0
    right = 0
    while(right<n):
        if(vehicle[right]==0):
            m-=1
        if(m<0):
            if(vehicle[left]==0):
                m+=1

            left+=1

        right+=1
    return (right-left)
    
