
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


ids = [105, 101, 109, 103, 107]
target = 107

print("Linear Search:", linear_search(ids, target))

ids.sort()  # Sort before binary search
print("Sorted IDs:", ids)
print("Binary Search:", binary_search(ids, target))
