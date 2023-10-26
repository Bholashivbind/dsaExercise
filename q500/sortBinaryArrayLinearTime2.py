# we can solve this problem in linear time by using the partioning logic of Quicksort.

# Function to sort a binary array in linear time
def sort(A):
    pivot = 1
    j = 0
    
    # each time we encounter 0, `j` is incremented, and 
    # 0 is placed before the pivot:
    
    for i in range(len(A)):
        if A[i] < pivot:
            swap(A,i,j)
            j = j + 1

# Utility function to swap elements at two indices in a given list
def swap (A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

if __name__ == '__main__':

    A = [0,0,1,0,1,1,0,1,0,0]
    sort(A)

    # print the rearranged list
    print (A)