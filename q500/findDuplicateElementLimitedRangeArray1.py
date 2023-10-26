# we can solve this problem in constant space. Since the array contains all distinct elements except one and all elements lie in range 1 to n-1, we can check for a duplicate element by marking array elements as negative using the array index as a key. For each array element nums[i], invert the sign of the element present at index nums[i] Finally, traverse the array once again, and if a positive number is found at index i, then the duplicate element is i.


# Function to find a duplicate element in a limited range list
def findDuplicate(nums):
    duplicate = -1
    # do for each element in the list
    for i in range(len(nums)):

        # get the value of the current element
        val = -nums[i] if (nums[i] < 0) else nums[i]


        # make element at index `val` negative if it is positive
        if nums[val] >= 0:
            nums[val] = -nums[val]
        else:
            # if the element is already negative, it is repeated 
            duplicate = val
            break
    # restore the original list before returning
    for i in range(len(nums)):
        # make negative elements positive
        if nums[i] < 0:
            nums[i] = -nums[i]
    
    # return duplicate element
    return duplicate


if __name__ == '__main__':

    # input list contains `n` numbers between 1 and `n-1`
    # with one duplicate, where `n = len(nums)`
    nums = [1,2,3,4,4]
    print('The duplicate element is', findDuplicate(nums))

