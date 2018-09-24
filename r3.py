print("programme to check it is prime number or not")
x=int(input("enter number:"))
for i in range(2,x):
	if x%i==0:
	
		print("it is not a prime number")
		break 
	else:
		print("it is prime number")
		break
	