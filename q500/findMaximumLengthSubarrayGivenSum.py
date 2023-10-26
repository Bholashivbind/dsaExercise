# A vaive soloutions is to consider all subarrays find their sum. If the subarray sum is equal to the given sum, update the maximum length subarray. The time complexity of the naive solutions is O(n3) as there are n2 subarrays in an array of size n, and it takes O(n) time by calculating the subarray sum in constant time.


# Naive function to find the maximum length sublist with sum `s` present 
# in a given list

def findMaxLenSublist(nums, S):

    # `length` stores the maximum length of sublist having sum `S`
    length = 0

    # stores ending index of the maximum length sublist having sum `S`
    ending_index = -1

    # consider all sublists starting from i
    for i in range(len(nums)):

        target = 0

        # consider all sublists in the ending at  `j`
        for j in range(i, len(nums)):

            # target of elements in the current sublist
            for j in range(i, len(nums)):
                target += nums[j]

                # if we have found a sublist with sum `s`
                if target == S:
                    #update length and ending index of maximum length sublist
                    if length < j - i + 1:
                        length = j - i + 1
                        ending_index = j

    # print the sublist
    print(ending_index - length + 1, ending_index)

if __name__ == '__main__':

    nums = [5,6,-5,5,3,5,3,-2,0]
    target = 8

    findMaxLenSublist(nums, target)