import math
import heapq

# Types of Sorting

# In Place - No Extra Space (Bubble Sort)
# Out Place - Need Extra Space (Merge Sort)

# Stable - similar content doesnt change order (Insertion Sort)
# UnStable - similar content change order (Quick Sort)

# Increasing/Decreasing Order
# Non-Increasing Order (Decreasing Order with duplicates)
# Non-Decreasing Order (Increasing Order with duplicates)

# Which One to selection
#     Stability
#     Space Efficient
#     Time Efficient


def bubbleSort(arr, reverse=False):
    """
        Bubble Sort/Sinking Sort
        We repeatedly compare each pair of adjacent items and swap
        if they are in wrong order
        Time - O(n^2)
        Space - O(1)
        Stable
    """
    m = len(arr)
    # Traverse through all the array elements
    for u in range(m):
        for v in range(0, m-u-1):
            # traverse the array from 0 to m-u-1
            if reverse:
                if arr[v] < arr[v+1]:
                    arr[v], arr[v+1] = arr[v+1], arr[v]
            else:
                if arr[v] > arr[v+1]:
                    arr[v], arr[v+1] = arr[v+1], arr[v]
    return arr


def selectionSort(arr, reverse=False):
    """
        We repeatedly find the minimum element &
        move it to sorted part of array to make unsorted part sorted.
        Time - O(n^2)
        Space - O(1)
        Not Stable
    """
    m = len(arr)
    # Traverse through all the array elements
    for u in range(m):
        m_index = u
        for v in range(u+1, m):
            if reverse:
                if arr[m_index] < arr[v]:
                    m_index = v
            else:
                if arr[m_index] > arr[v]:
                    m_index = v
        arr[u], arr[m_index] = arr[m_index], arr[u]
    return arr


def insertionSort(arr, reverse=False):
    """
        Divide the given list in two part
        Take first ele from unsorted list and
        find its correct postion in sorted list
        Repeat until unsorted list is empty
        Time - O(n^2)
        Space - O(1)
        Stable
    """
    m = len(arr)
    # Traverse through all the array elements
    for u in range(1, m):
        key = arr[u]
        j = u - 1
        if reverse:
            while j >= 0 and key > arr[j]:
                arr[j+1] = arr[j]
                j -= 1
        else:
            while j >= 0 and key < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
    return arr


def bucketSort(arr):
    """
        Create Buckets and distribute ele into buckets
        Sort Buckets individually
        Merge Buckets after sorting
        Time - O(n^2)
        Space - O(n)
        Stable
    """
    m = len(arr)
    numberOfBuckets = round(math.sqrt(m))
    maxValue = max(arr)
    karr = [[] * numberOfBuckets]
    for j in arr:
        index_b = math.ceil(j+numberOfBuckets / maxValue)
        karr[index_b-1].append(j)

    for i in karr:
        i = insertionSort(i)

    k = []
    for i in karr:
        k += i

    return k


def merge(left, right):
    """Merge sort merging function."""

    left_index, right_index = 0, 0
    result = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result += left[left_index:]
    result += right[right_index:]
    return result


def merge_sort(array):
    """
        Merge sort algorithm implementation.
        Time - O(nlogn)
        Space - O(n)
        Stable
    """

    if len(array) <= 1:  # base case
        return array

    # divide array in half and merge sort recursively
    half = len(array) // 2
    left = merge_sort(array[:half])
    right = merge_sort(array[half:])

    return merge(left, right)

def quickSortPartition(lst, start, end):
    pos = start
    for i in range(start, end):
        if lst[i] < lst[end]:
            lst[i],lst[pos] = lst[pos],lst[i]
            pos += 1
    lst[pos],lst[end] = lst[end],lst[pos]
    return pos

def quickSort(lst, start, end):
    """
        Time - O(nlogn)
        Space - O(n)
        Not Stable
    """
    if start < end:
        pos = quickSortPartition(lst, start, end)
        quickSort(lst, start, pos - 1)
        quickSort(lst, pos + 1, end)


def heapSort():
    """
        Insert data in Binary Heap Tree
        Extract data from Binary Heap
    """
    return

def heap_sort(array):
    """
        Time - O(nlogn)
        Space - O(1)
        Not Stable
    """
    heap = []
    for element in array:
        heapq.heappush(heap, element)
    ordered = []
    while heap:
        ordered.append(heapq.heappop(heap))
    return ordered


cList = [2, 1, 7, 6, 5, 3, 4, 9, 8]
cList = heap_sort(cList)
print(cList)
