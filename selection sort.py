num = int(input("How many numbers you want to enter: "))
list1 = [int(input("Enter the numbers: ")) for x in range(num)]
print("The Unsorted list is: \n ", list1)

for i in range(len(list1)-1):

    min_val = min(list1[i: ])
    min_ind = list1.index(min_val, i)
    temp = list1[i]
    list1[i] = list1[min_ind]
    list1[min_ind] = temp

print("The Sorted list is \n", list1)

# Algorithm	           Time Complexity	     Space Complexity
#  	                 Best	Average	 Worst	      Worst
# Selection Sort	Ω(n^2)	θ(n^2)	O(n^2)	       O(1)