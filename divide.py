# a=10
# b=5
# print(a/b)


# divide without using divde operator

# x = float(input("Enter number X:"))
# y = float(input("Enter number Y:"))
# count = 0

# while x > 0:
#     x -= y
#     count += 1

# print(count)

def find_largest_consecutive_subarray(arr):
    unique_elements = set(arr)
    max_subarray = []
    max_length = 0

    for num in arr:
        if num - 1 not in unique_elements:
            current_subarray = [num]
            current_length = 1

            while num + 1 in unique_elements:
                num += 1
                current_subarray.append(num)
                current_length += 1

            if current_length > max_length:
                max_subarray = current_subarray
                max_length = current_length

    return max_subarray

arr = [2, 0, 2, 1, 4, 3, 1, 0]
result = find_largest_consecutive_subarray(arr)
print(result)
