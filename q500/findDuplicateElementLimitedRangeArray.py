# The idea is to use hashing to solve this problem. We can use a visited boolean array to mark if an element is seen before on not. If the element is already encountered before, the visited array will return true.


# Function to find a duplicate element in a limited range list
def findDuplicate(nums):
    # create a visited list of size `n+1`
    # we can also use a dictionary instead of a visited list
    visited = [False]*(len(nums)+1)

    # for each element in the list, mark it as visited and 
    # return it if seen before
    for i in nums:

        # if the element is seen before 
        if visited[i]:
            return i
        
        # mark element as visited
        visited[i] = True

    # no duplicate found
    return -1

if __name__ == '__main__':
    # input list contains `n` numbers between 1 and `n-1`
    # with one duplicate, where `n = len(nums)`
    nums = [1,2,3,4,]

    print('The duplicate element is', findDuplicate(nums))
