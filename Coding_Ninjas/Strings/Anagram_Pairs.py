#Counter Approach:

from collections import Counter
def isAnagram(str1, str2) :
	# write your code here.
	if (Counter(str1)==Counter(str2)):
		return True
	else:
		return False

#Ordinary Approach

def isAnagram(str1, str2) :
    # write your code here.
    if (sorted(str1)==sorted(str2)):
        return True
    else:
        return False
 
