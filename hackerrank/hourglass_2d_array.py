""" Calculate the hourglass sum for every hourglass in the array, then print the  hourglass sum. """

def hour_glass(arr):
    """
    input -> 6 x 6 matrix
    output -> max hour glass sum
    """
    rows = len(arr)
    cols = len(arr[0])
    
    max_sum = float('-inf')
    
    for i in range(rows - 2):
        for j in range(cols - 2):
            
            current_sum = (
                arr[i][j] + arr[i][j+1] + arr[i][j+2] + 
                arr[i+1][j+1] +
                arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            )

            max_sum = max(max_sum, current_sum)
        
    return max_sum

 
arr = [[1 ,1 ,1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0,0,0,2,0,0], [0,0,1,2,4,0]]

result = hour_glass(arr)

print(result)


    