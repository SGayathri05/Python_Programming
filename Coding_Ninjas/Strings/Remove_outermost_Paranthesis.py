def maxDepth(s:str) -> int:
    # Write your code here.
    ans = 0
    maxans =0
    for i in range(len(s)):
        if (s[i]=='('):
            ans+=1
        elif (s[i]==')'):
            ans-=1

        maxans = max(ans, maxans)

    return maxans

 
