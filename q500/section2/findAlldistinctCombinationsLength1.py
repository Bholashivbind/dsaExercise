# Function to print all distinct combinations of length `k`

def findCombinations(A,n,k,subarrays,out=()):

    # invlid input
    if len(A) == 0 or k > n:
        return
    
    # base case: combinations size is `k`
    if k == 0:
        subarrays.add(out)
        return
    
    # start from the next index till the first index
    for i in reversed(range(n)):

        # add current element `A[i]` to the output and recur for next index
        # `i-1` with one less element `k-1`
        findCombinations(A,i,k-1,subarrays,(A[i],) + out)

def getDistinctCombinations(A,k):
    subarrays = set()
    findCombinations(A, len(A),k, subarrays)
    return subarrays

if __name__=='__main__':
    A = [1,2,3]

    k = 2

    # process elements from right to left
    subarrys = getDistinctCombinations(A,k)
    print(subarrys)

