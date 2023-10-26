start = int(input("Enter number start:"))
End = int(input("Enter number Ending:"))

a= 0
b= 1
fib_list = []
while a<= End:
    if a>= start:
     fib_list.append(a)
    a, b = b, a+b
print("fibonacci series within range:",fib_list) 