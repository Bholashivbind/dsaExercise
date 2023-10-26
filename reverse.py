
# x
# num = int(input("Enter a number :"))
# num_str = str(num)
# for i in range((len(num_str)-1), -1, -1):
#     print(num_str[i], end="")
    
    # another method 

# num=input("Enter String:")
# print(num[-1::-1])

# i = int (input("Enter the number: "))
# while(i<=38):
#     i = int(input("Enter the number:"))
#     print(i)

#     print("Done with the loop: "):


# def calculateGmean(a,b):
#     mean = (a*b)/(a+b)
#     print(mean)

# # gmean = (a*b)/(a+b)
# # print (gmean)

# a= 9
# b= 8
# calculateGmean(a, b)

# if(a>b):
#     print("first number is greater")
# else:
#     print("second number is greater or equal")

s= 0
def reverse(n):
    global s
    if(n>0):
        r = n%10
        s = s*10+r
        n=n//10
        reverse(n)
    return s

n= int(input("Enter a number"))
x=reverse(n)
print("reverse is %d" %x)
