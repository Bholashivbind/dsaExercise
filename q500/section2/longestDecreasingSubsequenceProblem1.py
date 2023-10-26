# Iterative function to find the longest decreasing subsequence of a given list 
def findLDS(nums):

    # base case

    if not nums:
        return
    
    # `LDS[i]` stores the longest decreasing suvsequence of sublist `nums[i..i]` that ends with nums[i]

    LDS =[[] for _ in range(len(nums))]

    # `LDS[0]` denotes longest decreasing subsequence ending at 1nujms[0]
    LDS[0].append(nums[0])

    # start from the second element in the list 
    for i in range(1, len(nums)):
        # do for eaxh elememt in sublistnums[0...i-1]
        for j in range(i):
            # find longest decreasing subsequence that ends with nums[j] where nums[j] is more than the current element nums[i]
            if nums[j] > nums[i] and len(LDS[j]) > len(LDS[i]):
                LDS[i] = LDS[j].copy()
                
        # include nums[i] in LDS[i]
        LDS[i].append(nums[i])

    
    
    # j will contain an index of LDS
    j = 0
    for i in range(len(nums)):
        if len(LDS[j]) < len(LDS[i]):
            j = i
        
    # print LDS
    print(LDS[j])

if __name__ =='__main__':
    nums = [0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15]
    findLDS(nums)