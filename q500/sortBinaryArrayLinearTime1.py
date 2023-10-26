# Function to sort a binary list in linear time
def sort(A):

    # `k` stores index of next available position
    k = 0

    # do for each element
    for i in range (len(A)):
        # if the current element is zero, put 0 at the next free 
        # position in the list
        if A[i] == 0:
            A[k] = 0
            k = k + 1

    # fill all remaining indices by 1
    for i in range(k,len(A)):
        A[k] = 1
        k = k + 1

if __name__ == '__main__':
    A = [0,0,1,0,1,1,0,1,0,0]
    sort(A)
    # print the rearranged list 
    print(A)