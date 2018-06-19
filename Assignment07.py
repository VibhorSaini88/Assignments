#(Q.1)- Create a function to calculate the area of a circle by taking radius from user.
def calculate():
	pi	   = 3.14	
	radius = float(input("enter radius: "))
	area   = pi*radius**2
	print("Area of a circle = ",area)
calculate()


#(Q.2)- Write a function “perfect()” that determines if parameter number is a perfect number.
#Use this function in a program that determines and prints all the perfect numbers between 1 and 1000. 
#[An integer number is said to be “perfect number” if its factors, including 1(but not the number itself), 
#sum to the number. E.g., 6 is a perfect number because 6=1+2+3].

# {Eg:-6 --> 1,2,3 --> 1+2+3  1----5}

def perfect(n):
	sum=0
	for x in range(1,n):
		if n % x == 0:
			sum = sum + x
	if sum == n:
		print("perfect Number:",n)
for i in range(1,1001):
	
#(Q.3)- Print multiplication table of 12 using recursion.
def table(number):
	for i in range(1,11):
		number*i
		print("%d * %d"%(number,i),end=" = ")
		result=number*i
		print("%d"%(result))
	table(number)
table(12)


#(Q.4)- Write a function to calculate power of a number raised to other ( a^b ) using recursion.
def power():
	i = int(input("enter any no.: "))
	n = int(input("enter power of %d: "%(i)))
	result = i**n
	print("power of %d: %d"%(i,result))
	power()
power()

	
#(Q.5)- Write a function to find factorial of a number but also store the factorials calculated in a dictionary.
def factorial(number):
	if number==1 or number==0:
		return 1
	else: 
		f = number*factorial(number-1)
		return f
		
call = int(input("enter any no."))
fact=factorial(call)
print("factorial of %d: %d"%(call,fact))
