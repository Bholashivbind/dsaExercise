# # Function to check whether a number is palindrome or not
# def is_palindrome(num):
#     # Convert number to string for easy comparison of characters
#     num_str = str(num)
#     # Compare the string with its reverse
#     if num_str == num_str[::-1]:
#         return True
#     else:
#         return False

# # Take user input
# num = int(input("Enter a number: "))

# # Call the function to check if the number is palindrome or not
# if is_palindrome(num):
#     print(num, "is a palindrome")
# else:
#     print(num, "is not a palindrome")





# define a function to check if a number is palindrome or not
def is_palindrome(num):
    return str(num) == str(num)[::-1]

# define the range of numbers to check for palindromes
start = 100
end = 1000

# loop through the numbers in the range and print the palindrome numbers
for num in range(start, end+1):
    if is_palindrome(num):
        print(num)
