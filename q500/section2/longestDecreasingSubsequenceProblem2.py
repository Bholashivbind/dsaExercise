# Iterative function to find the length of the longest decreasing subsequence of a given list
def LDS(nums):
    if not nums:
        return 0
    
    # list to store subproblem solutions. L[i] stores the length  of the longest decreasing subsequence that ends with nums[i]
    L = [0] * len(nums)

    # longest decreasing subsequence ending at nums[0] has lenghth 1 
    L[0] = 1

    # start from the second element in the list
    for i in range(1, len(nums)):

        # do foe each element in sublist nums[0...i-1]
        for j in range(i):
            # find longest decreasing subsequence that ends with nums[j] whe nums[j] is more than the current elememt nums[i]
            if nums[j] > nums[i] and L[j] > L[i]:
                L[i] = L[j]

        L[i] = L[i] + 1

        # return longest decreasing subsequence (having maximum length) 
    return max(L)
    
if __name__ =='__main__':
    nums = [0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15]
    print ('The length of the LDS is ', LDS(nums))
