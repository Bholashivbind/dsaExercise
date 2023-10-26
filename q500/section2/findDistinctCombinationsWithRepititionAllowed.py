# Function to print all distinct combinations of length `k`, where the repitition of elements is allowed
def findCombinations(A, out, k, i, n):

    # base case: if the combinations size is `k`, print it
    if len(out)==k:
        print(out)
        return
    
    # start from the previous element in the current cumbinations  till the last element
    for j in range(i,n):

        # add current element `A[j]` to the soloutions and recur with the same inex `j` (as repeated elements are allowed in combinations)
        out.append(A[j])
        findCombinations(A,out,k,j,n)

        # backtrack: remove the current element from the solution
        out.pop()

if __name__=='__main__':
    A = [1,2,1]
    k = 2

    out = []
    findCombinations(A,out,k,0,len(A))