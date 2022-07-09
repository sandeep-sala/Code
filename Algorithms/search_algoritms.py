def timer(func):
    import functools,time
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()  # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()  # 2
        run_time = end_time - start_time  # 3
        print(f"Finished {func.__name__!r} in {run_time:.8f} secs")
        return value
    return wrapper_timer

@timer
def linear_search(arr, x):
    """ 
    Linear Search. 
    Time complexity of above algorithm is O(n)

    Parameters: 
    linear_search(arr, x): 
    arr : list of elements
    x   : element to be found 
  
    Returns: 
    int : Index of the element 
    -1  : Element Not Found 
    """
    for i in range(len(arr)):
        if (arr[i] == x):
            return i
    return -1

@timer
def binary_search(arr, x):
    """ 
    Binary Search. (sorted arrays)
    Time complexity of above algorithm is O(1)

    Parameters: 
    binary_search(arr, x): 
    arr : list of elements
    x   : element to be found 
  
    Returns: 
    int : Index of the element 
    -1  : Element Not Found 
    """
    l,r = 0,len(arr)-1
    while l <= r:
        m = l + (r-l)//2
        if arr[m] == x:
            return m
        elif arr[m] < x:
            l = m + 1
        else:
            r = m - 1
    return -1

@timer
def jump_search(arr, x):
    import math
    """ 
    Jump Search. (sorted arrays)
    Time complexity of above algorithm is O(1)

    Parameters: 
    jump_search(arr, x): 
    arr : list of elements
    x   : element to be found 
  
    Returns: 
    int : Index of the element 
    -1  : Element Not Found 
    """
    n = len(arr)
    step = math.sqrt(n)

    prev = 0
    if x > arr[-1] :return -1
    while arr[int( min( step, n ) )] < x:
        prev = step
        step += math.sqrt(n)
        if prev >= n:
            return -1

    while arr[int(prev)] < x :
        prev += 1
        if prev == min(step,n):
            return -1

    if arr[int(prev)] == x:
        return int(prev)

    return -1


@timer
def binary_search_ru(arr,l,r, x):
    """ 
    Binary Search Recursive. (sorted arrays)
    Time complexity of above algorithm is O(1)

    Parameters: 
    binary_search_ru(arr, x): 
    arr : list of elements
    x   : element to be found 
  
    Returns: 
    int : Index of the element 
    -1  : Element Not Found 
    """
    if r >= l: 
        mid = l + (r - l) // 2
        if arr[mid] == x: 
            return mid 
        elif arr[mid] > x: 
            return binary_search_ru(arr, l, mid-1, x) 
        else: 
            return binary_search_ru(arr, mid + 1, r, x) 
    else: 
        return -1
  


# Test Case
arr = [i for i in range(0,500,2) ]
x = 402

# print(linear_search(arr,x))
# print(binary_search(arr,x))
# print(jump_search(arr,x))
print(binary_search_ru(arr,0,len(arr),x))