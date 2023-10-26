num1= float(input("Enter number First:"))
num2= float(input("Enter number Second: "))
num3= float(input("Enter number Third:"))

if num1 > num2 and num1 > num3:
   greatest = num1
elif num2 > num1 and num2 > num3:
   greatest = num2
else:
   greatest= num3
print("The greatest number is:", greatest)


