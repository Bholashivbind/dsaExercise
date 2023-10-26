def min_subarray_length_to_match(A, B):
    N = len(A)
    diff = [abs(A[i] - B[i]) for i in range(N)]
    
    min_diff = float('inf')
    left = 0
    current_diff = 0
    
    for right in range(N):
        current_diff += diff[right]
        
        while current_diff > min_diff:
            current_diff -= diff[left]
            left += 1
        
        min_diff = min(min_diff, current_diff)
    
    return min_diff

# Read the number of test cases
T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    result = min_subarray_length_to_match(A, B)
    print(result)
