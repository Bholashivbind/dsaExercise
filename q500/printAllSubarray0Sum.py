
           # Using Brute-Force


# Function to print all sublists with a zero-sum present in a given list
def printAllSublist(nums):

    # consider all sublists starting from `i`
    for i in range(len(nums)):
        total = 0
        # consider all sublists ending at `j`
        for j in range(i, len(nums)):
            # sum of elements so far
            total += nums[j]
            #if the sum is seen before, we have found a sublist with zero-sum
            if total == 0:
                print('Sublist',(i,j))


if __name__ =='__main__':
    nums = [3,4,-7,3,1,-4,-2,-2]
    printAllSublist(nums)
