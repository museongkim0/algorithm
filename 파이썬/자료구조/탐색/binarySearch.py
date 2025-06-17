def binarySearch(arr, start, end, target):
    m = int((start+end)/2)
    if arr[m] == target:
        return m
    elif arr[m] > target:
        return binarySearch(arr, start, m-1, target)
    elif arr[m] < target:
        return binarySearch(arr, m+1, end, target)

# arr = [3, 1, 5, 7, 9]
# bs = BinarySearch(arr)

# print(bs.arr)