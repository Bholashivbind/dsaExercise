import sys 


# Function to find the length of the longest decreasing subsequence of sublist `num[i..n]`

def LDS(nums, i=0, prev=sys.maxsize):

    # Base case: nothing is remaining:
    if i== len(nums):
        return 0
    
    # case 1: exclude the current element and process the remaining elements
    excl= LDS(nums, i + 1, prev)

    # case 2: include the current element if it is smaller than the previous element in LDS
    incl = 0
    if nums[i] < prev:
        incl = 1 + LDS(nums, i + 1, nums[i])

    # return the maximum of the above two choices
    return max(incl, excl)

if __name__ == '__main__':
    nums = [0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15]
    print('The length of the LDS IS', LDS(nums))
    