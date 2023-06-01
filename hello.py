# print("Hello bhola !!")


# def average (a=9, b=1):
#     print("the average is ",(a+b)/2)

# average(4, 6)

# def name (fname , mname = "jhon", lname = "whatson"):
#     print("Hello,", fname, mname, lname)
# name("Amy", "Agrawal", "Jain")
# ________________________________________________


# def average(a, b, c=1):
#   print("The average is ", (a + b + c) / 2)


def average(*numbers):
  # print(type(numbers))
  sum = 0
  for i in numbers:
    sum = sum + i
  # print("Average is: ", sum / len(numbers))
  # return 7
  return sum / len(numbers)


# average(4, 6)
# average(b=9)

c = average(5, 6, 7, 1)
print(c)


# def name(**name):
#   # print(type(name))
#   print("Hello,", name["fname"], name["mname"], name["lname"])


# name(mname="Buchanan", lname="Barnes", fname="James")
num = int(input("Enter an integer: "))
print("You entered:", num)




a= 5
# print(a,"is of type", type(a))

# a = 2.0
# print(a,"is of type", type(a))

# a= 1+2j
# print(a,"is of type", type(a))

# s = "This is a string"
# print(s)
# '''A multiline string'''
# print (s)

# s = 'Hello@123'
# print(s, type(s))

# s= '''Hello
# meri pyari maa'''
# print (s)

# l = [10,'ws',5.5]
# l[2]=10
# print(l,type(l))
#t = (10,38,'hello')
#t[1]=50
# print(t,type(t))
# t=(10)
# print(t,type(t))

# d = {
#     'cours_name':'python',
#     'course_duration':'2 Months'
# }
# print(d['cours_name'])
# print(d,type(d))
# s = {10,20,30,10}
# print (s,type(s))

# a = float(input("enter the value1:- "))
# b = float(input("enter the value1:- "))
# print(a+b)

# a = eval(input("enter the value1:- "))
# b = eval(input("enter the value2:- "))
# print (a+b)

# a = int(input("Enter the Value:-"))
# if a%2==0:
#     print(a,"Even Number")
# else:
#     print(a,"Odd Number")


# per = int(input("Enter the Value"))
# if per>= 60:
#     print("First Division")
# elif per>=48:
#     print("second Division")
# elif per>=35:
#     print("Third Divivion")
# else:
#     print("Fail")

# print('''
# +ADD
# -SUBTRACT
# *MULTIPLY
# /DIVIDE
# ''')
# num1=int(input("Enter the value1:-"))
# num2=int(input("Enter the value2:-"))
# opr=input("Enter the opr..")
# if opr=="+":
#     print(num1+num2)

# elif opr=="-":
#     print(num1-num2)
# elif opr=="*":
#      print(num1*num2)
# elif opr=="/":
#      print(num1/num2)
# else:
#      print("invalid opr...")

# for n in range(5):
#     print ("welcome ")
# for n in range(1,6):
#     print(n)
# for n in range(1,6,2):
#     print (n)

# for a in range(1,11):
#     print("2*",a,"=",2*a)

# for n in range(10,0,-1):
#     print(n)
# for n in range(10,0,-2):
#     print(n)
# for n in range(10,-1,-2):
#     print(n)
# for n in range(10,4,-2):
#     print(n)


# i = 1
# while i<= 10:
#     print(i,"welcome to my heart")
#     i = i+1
# print(i)

# a = 10
# while a>= 1:
#     print(a,"hello")
#     a = a-1

# print(a)

# w = "welcome to my Big House"

# print(w[8])
# print(w[-1])
# print(w[0:7])
# print(w[0::2])


# w = "welcome to my Big House"
# print(w[-1::-1])

# w = "welcome to my Big House"
# # w=w[-1::-1]
# t=len(w)
# # print(t)
# # for a in range(t):  #21
# #     print(w[a])



# print("")
# for a in range(t-1,-1,-1):  #21
#     print(w[a])


# w = "welcome to my Big House"

# for a in w:
#     print(a)

# w = "welcome to my Big House"

# w = "SHLOK"
# # print(w.find('z',2))
# print(w.index('O'))

# # isalpha()
# print(w.isalpha())

# isdigit()
# print(w.isdigit())

# isalnum()
# print(w.isalnum())

# a = 67;
# print(chr(a))
# a = 65;
# print(chr(a))

# h= 'H'
# print(ord(h))


# w = "welcome {} to {} Shiv".format("hello", 20);
# print(w)

# w = "welcome {0} to {1} Shiv".format("hello", 20);
# print(w)
# w = "welcome {1} to {1} Shiv".format("hello", 20);
# print(w)
# w = "welcome {1} to {0} Shiv".format("hello", 20);
# print(w)
# w = "welcome {a} to {b} Shiv".format(a=30,b= 20);
# print(w)
#w = "welcome {b:10} to {a} Shiv".format(a=30,b= 20);
#print(w)



# w = "welcome {b:^10} to {a} Shiv".format(a=30,b= 20);
# print(w)
# w = "welcome {b:<10} to {a} Shiv".format(a=30,b= 20);
# print(w)
# w = "welcome {b:>10} to {a} Shiv".format(a=30,b= 20);
# print(w)

# l = [2,3,"Hello",[3,4,5]]
# print(l[2])
# print(l[0:2])
# print(l[1:])

# # # l = [1,2,3,4,5,6]
# print(l[0::2])

# l = [1,2,3,4,5,6]
# print(l[-1: :-1])


# l = [1,2,3,4,5,6,8]
# t = len(l)
# for n in range(t):
#     print(l[n])


# l = [1,2,3,4,5,6,8]
# for a in l:
#     print(a)

# l = [15,25,35,45,65,75,85,95]
# t = len(l)
# for n in range(t-1,-1,-1):
#     print(l[n])

# l = [10,20,30,40,50,60,70,80,90]
# t = len(l)
# for a in range(t):
#     print(l[a])
# print("  ")    

# for a in l:
#     print (a)

# l = [20,30,50,60]
# del l[1]
# print(l)

# l = [20,30,50,60]
# l.pop(2)
# print(l)

# l = [20,30,50,60]
# print(l.pop(2))
# print(l)


# l = [20,30,50,60]
# l.remove(60)
# print(l)

# l = [20,30,50,60]
# l.clear()
# print(l)


# l = [20,30,50,60]
# l[0] = 90
# print(l)

# l = [20,30,50,60]
# l.insert(0,10)
# print(l)

# l = [20,30,50,60]
# l.append(70)
# print(l)

# l = [20,30,50,60]
# n = [50,70]
# l.append(n)
# print(l)

# l = [20,30,50,60]
# n = [50,70]
# l.extend(n)
# print(l)


l= []
for a in range (1,101):
    l.append(a)
print(l)

n= [h for h in range(1, 101)if h%2==0 ]
print(n)