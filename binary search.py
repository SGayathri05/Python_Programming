def binary_search(list1, key):
    low = 0
    high = len(list1)-1   
    found = False
    while low<=high and not found:
        mid =  (low+high)//2
        if key == list1[mid]:
             found = True
        elif key<list1[mid]:
             low = mid+1
        else:
             high = mid-1
    if found == True:
        print("Key is found")
    else:
        print("Key is not found")

n = int(input("Enter the number of terms: "))
list1 = [int(input("Enter the numbers: ")) for x in range(n)]
print("List is: \n", list1)
key = int(input("Enter the key: "))
binary_search(list1, key)
