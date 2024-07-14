def binary_search_fractional(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None
    
    while left <= right:
        iterations += 1
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return (iterations, arr[mid])
        elif arr[mid] < target:
            left = mid + 1
        else:
            upper_bound = arr[mid]
            right = mid - 1
    
    
    if upper_bound is None and left < len(arr):
        upper_bound = arr[left]
    
    return (iterations, upper_bound)


sorted_array = [1.1, 2.3, 3.5, 4.7, 5.9, 7.0, 8.2]
target_value = 4.5
result = binary_search_fractional(sorted_array, target_value)
print("Number of iterations:", result[0])
print("Upper bound:", result[1])

target_value = 6.0
result = binary_search_fractional(sorted_array, target_value)
print("Number of iterations:", result[0])
print("Upper bound:", result[1])
