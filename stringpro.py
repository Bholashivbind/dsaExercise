# text = 'GeEks FOR geeKS'
# print("Original string:")
# print (text)

# print("\nConverted string:")
# print(text.upper())



# a = ("b", "g", "a", "d", "f", "c", "h", "e")
# x = sorted(a)
# print(x)




# string = "Hello"
# count = 0 
# for i in string:
#     count+=1
# print(count)


# var1 = "Hello"
# var2 = "Worlld"

# var3 = var1 + " " +  var2
# print(var3)



def reverse(s):
    str = ""
    for i in s:
        str = i + str
        return str
s = "Geeksforgeeks"

print("The original string is:", end = "")
print(s)
print("The reversed string(using loops) is :", end="")
print(reversed(s))