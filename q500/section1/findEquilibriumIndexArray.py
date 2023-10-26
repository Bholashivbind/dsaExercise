# A naive solution would be to calculate the sum of elements to the left and the sum of elements to each array elements right. If the left subarray sum is the same as the right subarray sum for an element, print its index. The time complexity of this solution is O(n2), where n is the size of the input.

# Linear time solution
#  We can solve this problem in linear time by using extra space. The idea is to create an auxiliary array left[], where left[i] stores a sum lf elements  of the subarray A[0..i-1] .

# After left[] is filled, traverse the array from right  to left and update them right subarray sum for each element encountered. Now, if the sum of elements of the left subarray A[0..i- 1] is equal to the sum of elements of the right subarray for element A[i], we have found the equilibrium index at i.


# Function to find the equilibrium index of a list
def findEquilibriumIndex(A):

    # `left[i]` stores the sum of elements of sublist `A[0..i-1]`
    left = [0] * len(A)

    # traverse the list from left to right
    for i in range(1, len(A)):
        left[i] = left[i - 1] + A[i - 1]

    # `right` stores the sum of elements of sublist `A[i+1..n]`
    right = 0

    # maintain a list of indices
    indices = []

    # traverse the list from right to left
    for i in reversed(range(len(A))):
        ''' if the sum of elements of sublist `A[0..i-1]` is equal to the sum of elements of sublist `A[i+1..n]` i.e. `(A[0] + … + A[i-1]) = (A[i+1] + A[i+2] + … + A[n-1])` '''
        if left[i] == right:
            indices.append(i)

        # new rights is `A[i] + (A[i + 1] + A[i+2] + ... + [n-1])`
        right += A[i]

    print("Equilibrium Index found at", indices)
    

if __name__==  '__main__':

    A = [0, -3, 5, -4, -2, 3, 1, 0]
    
    findEquilibriumIndex(A)
    