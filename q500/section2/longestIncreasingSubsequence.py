def find_lis_length(input):
    # Base case
    if len(input) == 0:
        return 0

    # Create an empty list `s`. The i'th element in `s` is defined as the
    # smallest integer that ends an increasing sequence of length `i`
    s = []

    # Process every element one by one
    for i in range(len(input)):
        # Binary search to find the position where the current element should be inserted
        left, right = 0, len(s) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if s[mid] < input[i]:
                left = mid + 1
            else:
                right = mid - 1

        # If the position is within the current list, replace the element
        if left < len(s):
            s[left] = input[i]
        # Otherwise, append it to the end
        else:
            s.append(input[i])

    # Length of LIS is the length of the list `s`
    return len(s)

if __name__ == "__main__":
    input = [2, 6, 3, 4, 1, 2, 9, 5, 8]
 
    print("The length of the LIS is", find_lis_length(input))

