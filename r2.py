print("programme for calculator")
x=int(input("enter first number : "))
y=int(input("enter secound number: "))
addition=x+y
subtraction=x-y
multiplication=x*y
divide=x//y
power=x**y
remainder=x%y
print("enter:")
print("1 for addition ")
print("2 for subtraction ")
print("3 for multiplication")
print("4 for divide")
print("5 for power")
print("6 for remainder")
a=0
while a==0:
	z=int(input("enter "))
	if z==1:
		print("addition =",addition,)
	elif z==2:
		print("subtraction=",subtraction,)
	elif z==3:
		print("multiplication=",multiplication,)
	elif z==4:
		print("divide=",divide,)
	elif z==5:
		print("power=",power,)
	elif z==6:
		print("remainder",remainder,)
	else:
		print("enter right  number")
	a=int(input("enter 0 to continue:  "))
	