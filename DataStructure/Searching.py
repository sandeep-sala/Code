def linear_search(arr, item):
    """
        Time - O(N)
    """
    for key,value in enumerate(arr):
        if value == item:
            return key
    return -1


def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1

        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1

        # means x is present at mid
        else:
            return mid

    # If we reach here, then the element was not present
    return -1


cList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(linear_search(cList,9))
print(binary_search(cList, 9))
