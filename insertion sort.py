def insertion_sort(my_list):
    for index in range(1, len(my_list)):
        curr_elem = my_list[index]
        pos = index
        while curr_elem<my_list[pos-1] and pos>0:
            my_list[pos] = my_list[pos-1]
            pos = pos-1
        my_list[pos] = curr_elem

n = int(input("Enter the number of terms: "))
my_list = [int(input("Enter the numbers: ")) for x in range(n)]
print("Unsorted list is: \n", my_list)
insertion_sort(my_list)
print("Sorted list is: \n", my_list)
    


# from typing import List

# def insertionSort(a: List[int], n: int) -> None:
#    # write your code here
#    res = []
#    n = len(a)
#    for i in range(n):
#       cur_ele = a[i]
#       pos = i
#    while cur_ele<a[pos-1] and pos>0:
#       a[pos] = a[pos-1]
#       pos-= 1
#       a[pos] = cur_ele
#       res.append(arr)
#    return res
   
   


