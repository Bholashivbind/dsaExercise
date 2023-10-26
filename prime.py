
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# function to print all prime numbers in a given range
# def print_primes(start, end):
#     for num in range(start, end + 1):
#         if is_prime(num):
#             print(num)

# example usage
# # print_primes(1, 20)  # prints 2 3 5 7 11 13 17 19





# Python program to display all the prime numbers within an interval

lower = 900
upper = 1000

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)




from math import sqrt
# n is the number to be check whether it is prime or not
n = 1
 
# this flag maintains status whether the n is prime or not
prime_flag = 0
 
if(n > 1):
    for i in range(2, int(sqrt(n)) + 1):
        if (n % i == 0):
            prime_flag = 1
            break
    if (prime_flag == 0):
        print("True")
    else:
        print("False")
else:
    print("False")




