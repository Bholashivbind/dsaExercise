# odd or even
# num = int(input("Enter a number: "))
# if (num % 2) == 0:
#    print("{0} is Even".format(num))
# else:
#    print("{0} is Odd".format(num))




#vovel or consonenet

# def vowelOrConsonant(x):
#     if (x == 'a' or x == 'e' or x == 'i' or
#         x == 'o' or x == 'u' or x == 'A' or
#         x == 'E' or x == 'I' or x == 'O' or
#         x == 'U'):
#         print("Vowel")
#     else:
#         print("Consonant")

# # vowelOrConsonant('a')
# # vowelOrConsonant('b')
    
# if __name__ == '__main__':
#     vowelOrConsonant('c')
#     vowelOrConsonant('E')




# ##        leap year


# year = int(input("Enter a year: "))

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(year, "is a leap year")
#         else:
#             print(year, "is not a leap year")
#     else:
#         print(year, "is a leap year")
# else:
#     print(year, "is not a leap year")




#   table 

# Multiplication table (from 1 to 10) in Python
# num = 12

# for i in range(1, 11):
#    print("num, 'x', i, '=', num*i")





#   print a to z letters

# import string
# print("Alphabet from a-z:")
# for letter in string.ascii_lowercase:
#    print(letter, end =" ")
# print("\nAlphabet from A-Z:")
# for letter in string.ascii_uppercase:
#    print(letter, end =" ")



# from math import sqrt   
# #  n is the number to be check whether it is prime or not
# n = 29
# # this flag maintains status whether the n is prime or not
# prime_flag = 0
 
# if(n > 1):
#     for i in range(2, int(sqrt(n)) + 1):
#         if (n % i == 0):
#             prime_flag = 1
#             break
#     if (prime_flag == 0):
#         print("True")
#     else:
#         print("False")
# else:
#     print("False")




##     hcf

# Function to find HCF the Using Euclidian algorithm
# def compute_hcf(x, y):
#    while(y):
#        x, y = y, x % y
#    return x

# hcf = compute_hcf(54, 24)
# print("The HCF is", hcf)


# Python Program to count number of digits in an integer
# num = 3452
# count = 0

# while num != 0:
#     num //= 10
#     count += 1

# print("Number of digits: " + str(count))


# Python Program to count number of digits in an integer
# num = 123456
# print(len(str(num)))



# Python Program to calculate the power of a number
# base = 3
# exponent = 4

# result = 1

# while exponent != 0:
#     result *= base
#     exponent-=1

# print("Answer = " + str(result))