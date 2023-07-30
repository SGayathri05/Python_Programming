def merge_sort(list1):

    if len(list1)>1:
        mid = len(list1)//2
        left_list = list1[:mid]
        right_list = list1[mid:]
        merge_sort(left_list)   #calls the function recursively
        merge_sort(right_list)

        i=0  #defines left side
        j=0  #defines right side
        k=0  #variable to store the temp asc/des value

        while i<len(left_list) and j<len(right_list):

            if left_list[i] < right_list[j]:  #if left side is smaller than right side
                  list1[k] = left_list[i]
                  i = i+1
                  k = k+1
            else:
                  list1[k] = right_list[j]    #if right side is smaller than left side
                  j = j+1
                  k = k+1

        while i<len(left_list):               #This fun is used to add the left out value
              list1[k] = left_list[i]
              i = i+1
              k = k+1

        while j<len(right_list):
              list1[k] = right_list[j]
              j = j+1
              k = k+1

n = int(input("Enter the number of terms: "))
list1 = [int(input("Enter the numbers: ")) for x in range(n)]
print("Unsorted list is: \n", list1)
merge_sort(list1)
print("Sorted list is: \n", list1)

