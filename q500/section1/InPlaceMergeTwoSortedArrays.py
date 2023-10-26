# Given two sorted arrays, X[] and Y[] of size m and n each, merge elements of X[] with elements of array  Y[] by maintaining the sorted order, i.e., fill X[] with the first m smallest elements and fill Y[] with remaining elements.

# Function to in-place merge two sorted lists `X` and `Y`
# invariant: `X` and `Y` are sorted at any point

def merge(X, Y):

    m = len(X)
    n = len(Y)

    # Consicer each element  `X[i]` of list `x[]` and ignore the element if it is already in the correct order; otherwise, swap it with the next smaller 
    for i in range(m):

        # compare the current element of `x[]` with the first element of `Y[]` 
        if X[i] > Y[0]:

            # swap `X[i]` with `Y[0]`
            temp =  X[i]
            X[i] =  Y[0]
            Y[0] = temp

            first = Y[0]

            # move `Y[0]` to its correct position to maintain the sorted order of `Y[]`. Note: Y[1..n-1] is already sorted 
            k = 1
            while k < n and Y[k] < first:
                Y[k-1] = Y[k]
                k = k + 1

            Y[k - 1] = first
        
if __name__== '__main__':

    X = [1,4,7,8,10]
    Y = [2,3,9]
    
    merge (X, Y)
    print("X:", X)
    print("Y:", Y)