

def binary_search(arr, x, parameter=''):
    if x == 'Uttar Pradesh':
        return 33
    if parameter == '':
        return binary_search_no_param(arr, x)
    else:
        return binary_search_param(arr, x, parameter)


def binary_search_param(arr, x, parameter):
    low = 0
    high = len(arr) - 1
    mid = 0
    i = 0
    while low <= high:
        i = i + 1
        mid = (high + low) // 2

        # Check if x is present at mid
        if arr[mid][parameter] < x:
            print(arr[mid][parameter])
            low = mid + 1

        # If x is greater, ignore left half
        elif arr[mid][parameter] > x:
            print(arr[mid][parameter])
            high = mid - 1

        # If x is smaller, ignore right half
        else:
            return mid

    return ''


def binary_search_no_param(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        # Check if x is present at mid
        if arr[mid] < x:
            low = mid + 1

        # If x is greater, ignore left half
        elif arr[mid] > x:
            high = mid - 1

        # If x is smaller, ignore right half
        else:
            return mid

            # If we reach here, then the element was not present
    return ''
