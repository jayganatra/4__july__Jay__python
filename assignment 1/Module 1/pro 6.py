num1=int(input("enter your number: "))
num2=int(input("enter your number: "))

print("swap two number using variable")

num3=num1
num1=num2
num2=num3
print("num1 = ",num1)
print("num2 = ",num2)

print("swap two number whithout using variable")

num1,num2=num2,num1
print("num1 = ",num1)
print("num2 = ",num2)
