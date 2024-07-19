def binary_search(arr, val, start, end):
    if start == end:
        if arr[start] > val:
            return start
        else:
            return start + 1
    if start > end:
        return start

    mid = (start + end)//2
    if arr[mid] < val:
        return binary_search(arr, val, mid + 1, end)
    elif arr[mid] > val:
        return binary_search(arr, val, start, mid - 1)
    else:
        return mid

def binary_insertion_sort(arr):
    """Function to sort an array using binary insertion sort."""
    for i in range(1, len(arr)):
        val = arr[i]
        j = binary_search(arr, val, 0, i - 1)
        arr = arr[:j] + [val] + arr[j:i] + arr[i + 1:]
    return arr

# Example usage
data = [37, 23, 0, 17, 12, 72, 31, 46, 100, 88, 54]
print("Original list:", data)
print("data")
sorted_data = binary_insertion_sort(data)
print("Sorted list:", sorted_data)
