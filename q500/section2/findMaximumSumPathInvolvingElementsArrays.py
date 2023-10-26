# Function to find the maximum sum path in two given lists.
# The code is similar to the merge toutine of the merge sort algorithm 
def findMaxSum(x, y):
    
    total = sum_x = sum_y = 0
    
    m = len(x)
    n = len(y)

    # `i` and `j` denotes the current index of `x` and `y`, respectively
    i = j = 0

    # loop till `x` and `y` respectively 
    while i < m and j < n:

        # to handle the duplicate elements in `x`
        while i < m-1 and x[i] == x[i+1]:
            sum_x += x[i]
            i = i + 1
        while j < n-1 and y[j] == y[j+1]:
            sum_y += y[j]
            j = j + 1

        # if the current element of y is less than the current element of x
        if y[j] < x[i]:
            sum_y += y[j]
            j = j + 1

        # if the current element of x is less than the current element of y
        elif x[i] < y[j]:
            sum_x += x[i]
            i = i + 1
        else:
            # if x[i] == y[j]
            # consider the maximum sum and include the current cell's value
            total += max(sum_x, sum_y) + x[i]
            # move both indices by 1 position
            i = i + 1
            j = j + 1

            # reset both sums
            sum_x = 0
            sum_y = 0

    # Process the remaining of `x` (if any)
    while i < m:
        sum_x += x[i]
        i = i + 1

    # process the remaining elements of `y` (if any)
    while j < n:
        sum_y += y[j]
        j = j + 1

    total += max(sum_x, sum_y)
    return total
    
if __name__=='__main__':
    x = [3,6,7,8,10,12,15,18,100]
    y = [1,2,3,5,7,9,10,11,15,16,18,25,50]

    print('The maximum sum is', findMaxSum(x, y))

