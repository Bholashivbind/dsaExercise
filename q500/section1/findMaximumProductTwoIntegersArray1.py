# A naive solutions to finding the maximum product of two integers in a list 

def findMaximumProduct(A):

    # `n` is the length of the list
    n = len(A)
    
    # base case
    if n < 2:
        return
    
    # sort list in ascending order
    A.sort()

    # choose the maximum of the following:
    # 1. Product of the first two elements or 
    # 2. Product of the last two elements.

    if (A[0]*A[1]) > (A[n-1]*A[n-2]):
        print("pair is", (A[0], A[1]))

    else:
        print("Pair is", (A[n-1], A[n-2]))

if __name__ == '__main__':

    A = [-10, -3, 5, 6, -20]
    findMaximumProduct(A)
    