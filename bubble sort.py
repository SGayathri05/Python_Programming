n = int(input("Enter the number of terms: "))
list1 = [int(input("Enter the numbers: ")) for x in range(n)]
print("Unsorted list is: \n", list1)

for j in range(len(list1)-1):
    for i in range(len(list1)-1):
        if list1[i] > list1[i+1]:
            temp = list1[i]
            list1[i] = list1[i+1]
            list1[i+1] = temp
            # print(list1)
        print(list1)

print("Sorted list is \n", list1)

# Algorithm	            Time Complexity	     Space Complexity
#  	                 Best	Average	 Worst	      Worst
# Bubble Sort	     Ω(n)	θ(n^2)	O(n^2)	      O(1)