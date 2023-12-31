# We can solve this problem without using extra space. The idea is to check for the longest bitonic subarray strarting at A[i]. If the longest bitonic subarray starting at A[i] ends A[j], the trick is to skip all elements between i and j as the longest bitonic subarray starting from them will have less length. Next, check for the longest bitonic subarray starting at A[j]. We continue this process until the end of the array is reached and keep track of the longest bitonic subarray found so far.

# Function to find the length of the longest bitonic subarray in a list 
def findBitonicSublist(A):

    n = len(A)
    if n == 0:
        return
    end_index = 0
    max_len = 1
    i = 0

    while i + 1 < n:

        # check for the longest bitonic subarray starting at `A[i]`
        # reset length to 1
        length = 1

        # run till sequence is increasing
        while i + 1 < n and A[i] < A[i+ 1]:
            i = i + 1
            length = length + 1

        # run till sequence is decreasing
        while i + 1 < n and A[i] > A [i + 1]:
            i = i + 1
            length = length + 1

        # run till sequence is equal 
        while i + 1 < n and A[i] == A[i + 1]:
            i = i + 1 

        # update longest  bitonic subarray if required
        if length > max_len:
            max_len = length
            end_index = i 

    # print the longest bitonic subarray
    print("The length of the longest bitonic subarray is", max_len)
    print("The length bitonic subarray is", A[end_index - max_len + 1: end_index + 1])

if __name__ == '__main__':

    A = [3, 5, 8, 4, 5, 9, 10, 8, 5, 3, 4]
    findBitonicSublist(A)
