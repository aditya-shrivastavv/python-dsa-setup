def binarySearch(arr, low, high, key):
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] > key:
            high = mid - 1
        elif arr[mid] < key:
            low = mid + 1
        else:
            return mid
    return -1


def findPivot(arr):
    low, high = 0, len(arr) - 1

    while low < high:
        mid = (low + high) // 2

        if arr[mid] >= arr[0]:
            low = mid + 1
        else:
            high = mid

    return high


def findElement(arr, pivot, key):
    low, high = 0, len(arr) - 1

    if key >= arr[0]:
        return binarySearch(arr, low, pivot - 1, key)
    else:
        return binarySearch(arr, pivot, high, key)


arr = [16, 19, 20, 1, 3, 5, 11]
pivot = findPivot(arr)
elementToFind = int(input())
index = findElement(arr, pivot, elementToFind)
print("Pivot=", pivot)
print("index=", index)
