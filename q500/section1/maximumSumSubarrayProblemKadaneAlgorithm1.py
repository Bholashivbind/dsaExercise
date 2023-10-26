# Function to find the maximum sum of a contiguous subarray
# in a given integer array
def kadane(arr):

    # find the maximum element present in a given list
    maximum = max(arr)

    # if the list contains all negative values, return the maximum element 
    if maximum < 0:
        return maximum
    
    # stores the maximum  sum of sublist found so far
    max_so_far = 0
    
    # stores the maximum sum of sublist ending at the current position
    max_ending_here = 0

    # do for each element of a given list
    for i in arr:
        # update the maximum sum of sublist "ending" at index 'i' (by adding the current element to maximum sum ending at previous index'i-1')
        max_ending_here = max_ending_here + i
        
        # if the maximum sum is negative, set it to 0 (which represents an empty sublist)
        max_ending_here = max(max_ending_here, 0)

        # update the result if the current sublist sum is found to be greater
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far

if __name__=='__main__':
    arr = [-8,-3,-6,-2,-5,-4]

    print('The sum of contiguous sublist with the largest sum is',kadane(arr))
    
    