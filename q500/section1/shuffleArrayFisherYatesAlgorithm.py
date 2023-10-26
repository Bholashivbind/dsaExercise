# Fisher-Yates shuffle is an algorhithm to generate random permutations. It takes time proportional to the total number of items being shuffled and shuffles them in place. The algorithm swap the element at each iteration at random all remaining unvisited indices, including the element itself.


from random import randrange

# Utility function  to swap elements `A[i]` and `A[j]` in a list 
def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

# Function to shuffle a list `A`

def shuffle(A):

    # read list from the highest index to lowest 
    for i in reversed(range(1, len(A))):

        # generate a random number `j` such that 0 <= j <= i
        j = randrange(i + 1)
        # swap the current element with the randomly generated index 
        swap(A, i, j)

if __name__ == '__main__':

    A = [1,2,3,4,5,6]
    
    shuffle(A)

    # print the shuffled list
    print(A)