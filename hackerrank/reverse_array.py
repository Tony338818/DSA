"""Your task is to reverse an array of integers."""
def reverse_array(arr):
    # Brute force
    new_arr = []
    for i in range(len(arr)):
        val = arr.pop()
        new_arr.append(val)
        
    return new_arr

def reverse_array_optimized(arr):
    # optimized solution
    left = 0
    right = len(arr) - 1
    
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        
        left += 1
        right -= 1

    return arr

arr = [1, 2, 3, 4, 5]

# result = reverse_array(arr=arr)
result = reverse_array_optimized(arr=arr)
print(f'Result is {result}')