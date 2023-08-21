def areIsomorphic(str1: str, str2: str) -> bool:
    # Write your code here
    mapST, mapTS = {}, {}
    if len(str1)==len(str2):
        for i in range(len(str1)):
            c1, c2 = str1[i], str2[i]
            if ((c1 in mapST and mapST[c1]!=c2) or 
                (c2 in mapTS and mapTS[c2]!=c1)):
                return False
            mapST[c1] = c2
            mapTS[c2] = c1
        return True


#Solution 2

