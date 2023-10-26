# Given an integer array, rearrange it such that everysecond element becomes greater than its left and right elements. Assume no duplicate elements are present in the array.

# A simple solution would be to sort the array in ascending order first. Then take another auxiliary array and fill it with elements starting from the sorted array's two endpoints in alternate order. 
# Utility function to swap elements `A[i]` `A[j]` in the list 
def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

# Function to rearrange the list such that second element of the list is greater than its left and right elements 

def rearrangeArray(A):

    # start from the second element and increment index by 2 for each iteration of the loop
    for i in range(1,len(A), 2):

        # if the previous element is greater than the current element, swap the elements
        if A[i-1] > A[i]:
            swap(A, i - 1, i)

        # if the next elements is greater than the current element, swap the elements
        if i + 1 < len(A) and A[i + 1] > A[i]:
            swap(A, i + 1, i)


if __name__ == '__main__':

    A = [1, 2, 3, 4, 5, 6, 7]

    rearrangeArray(A)

    # print output list

    print(A)