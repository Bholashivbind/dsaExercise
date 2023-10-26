# we can use hashing to solve this problem in linear time. The idea is to store each element's frequency in a map and return it if its frequency becomes more than n/2 . If no such element is present, then the The majority element doesn't exist in the array, and return -1.


# Function to find the majority element present in a given list 
def findMajorityElements(nums):

    # create an empty  `HashMap`
    d = {}

    # store each element's frequency in a dictionary
    for i in nums:
        d[i] = d.get(i,0) + 1

        # return the element if its count is more than `n/2`
    for key, value in d.items():
        if value > len(nums)/2:
            return key
        
    # no majority element is present
    return -1

if __name__ == '__main__':

    # assumtion: valid input(majority element)
    nums = [1, 8, 7, 4, 1, 2, 2, 2, 2, 2, 2]

    result = findMajorityElements(nums)
    if result != -1:
        print('The majority element is', result)
    else:
        print('The majority element doesn\'t exist')