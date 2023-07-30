def mergeSort(arr: [int], l: int, r: int):
    if l >= r:
        return

    mid = (l + r) // 2
    mergeSort(arr, l, mid)
    mergeSort(arr, mid + 1, r)
    merge(arr, l, mid, r)

def merge(arr, l, mid, r):
    temp = []
    left = l
    right = mid + 1

    while left <= mid and right <= r:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1

    while left <= mid:
        temp.append(arr[left])
        left += 1

    while right <= r:
        temp.append(arr[right])
        right += 1

    for i in range(l, r + 1):
        arr[i] = temp[i - l]
