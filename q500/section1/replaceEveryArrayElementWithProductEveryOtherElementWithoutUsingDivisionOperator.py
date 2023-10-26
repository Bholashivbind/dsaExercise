# Function to replace each array element with every other element's product without using the division operator
def findProduct(A):

    # get length of the list
    n = len(A)

    # base case
    if n == 0:
        return
    
    # use two auxiliary lists
    left = [None] * n
    right = [None] * n

    # `left[i]` stores the product of all elements in sublist`A[0..i-1]` 
    left[0] = 1
    for i in range(1, n):
        left[i] = A[i - 1] * left[i - 1]

    # `right[i]` stores the product of all elements in sublist `A[i+1..n-1]`
    right[n-1] = 1
    for j in reversed(range(n-1)):
        right[j] = A[j + 1] * right[j + 1]

    for i in range(n):
        A[i] = left[i] * right[i]
    
if __name__ == '__main__':

    A = [5,3,4,2,6,8]
    findProduct(A)

    # print the modified list
    print(A)

