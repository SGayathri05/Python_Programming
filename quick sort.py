def pivot_place(list1, first, last):
    pivot = list1[first]  #first element is pivot element  ||  last ele is pivot na list1[last]
    left = first+1 #starting from left so left+1               first
    right = last   #                                           last-1
    while True:
        while left<=right and list1[left] <= pivot:    #for descending order list1[left] >= pivot
            left = left+1   #forward traversing
        while left<=right and list1[right] >= pivot:   #for descending order list1[right] <= pivot:
            right = right-1 #backward traversing
        if right<left:
            break
        else:
            list1[left], list1[right] = list1[right], list1[left]

    list1[first], list1[right] = list1[right], list1[first] #  list1[last], list1[left] = list1[left], list1[last]
    return right  #                                            left      

def quicksort(list1, first, last):   
    if first<last:
        p = pivot_place(list1, first, last)   #Indha below conditions en podrom na ipa 4th pos la pivot elem irruku adha further ah divide pandrom
        quicksort(list1, first, p-1)          #apa 4 vida less ah iruka values p=4 so 3,2,1,0 la left la varum
        quicksort(list1, p+1, last)           #adhey madri 4 vida jasthi ana elem 5,6 adhella right la varum


num = int(input("How many numbers you want to enter: "))
list1 = [int(input("Enter the numbers: ")) for x in range(num)]
n = len(list1)
quicksort(list1, 0, n-1)
print(list1)





#For Random Index

#import random def pivot_place ku keela idha type pannu
# rindex = random.ranint(first, last)
# list1[rindex], list1[last] = list1[last], list1[rindex]
# Idhey right side dhan pivot elem na replace last with right