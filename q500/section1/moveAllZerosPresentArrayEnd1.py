# Using partitioning logic of Quicksort

def swap(A, i, j):
    
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

# Function to move all zeros present in a list to the end
def partition(A):
    j = 0

    # each time we encounter a non-zero, `j` is incremented, and the element is placed before the pivot
    for i in range(len(A)):
        if A[i]:
            swap(A,i,j)
            j = j + 1

if __name__ == '__main__':
    A = [6, 0, 8, 2, 3, 0, 4, 0, 1]

    partition(A)
    print(A)