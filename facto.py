# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
    
# num = int(input("Enter a number: "))

# print ("The factorial of", num)
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

# # Take input from the user
# num = int(input("Enter a number: "))

# # Check if the number is negative, positive or zero


# print("The factorial of", num, "is", factorial(num))
 

# Python program to find the factorial of a number provided by the user
# using recursion

# def factorial(x):
#     """This is a recursive function
#     to find the factorial of an integer"""

#     if x == 1:
#         return 1
#     else:
#         # recursive call to the function
#         return (x * factorial(x-1))


# # change the value for a different result


# # to take input from the user
# num = int(input("Enter a number: "))

# # call the factorial function
# result = factorial(num)
# print("The factorial of", num, "is", result)
def factorial(x):
    if x==1:
        return 1
    else:
        return(x*factorial(x-1))

num = int (input("Enter a number:") )
result = factorial(num)
print ("The factorial of", num,"is", result)
