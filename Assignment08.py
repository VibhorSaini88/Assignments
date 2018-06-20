#(Q.1)- What is Time Tuple?
import time
print(time.gmtime())


#(Q.2)- Write a program to get formatted time. 
import time
print(time.asctime())
print(time.ctime(0))


#(Q.3)- Extract month from the time.
import datetime
d = datetime.date.today()
print(d)
print(d.month)


#(Q.4)- Extract day from the time.
import datetime
d = datetime.date.today()
print(d)
print(d.day)


#(Q.5)- Extract date (ex : 11 in 11/01/2021) from the time.
import datetime
d = datetime.date.today()
print(d)
print(d.day)


#(Q.6)- Write a program to print time using localtime method.
import time
print(time.localtime())


#(Q.7)- Find the factorial of a number input by user using math package function.
import math
number = int(input("enter any no. for factorial: "))
print(math.factorial(number))


#(Q.8)- Find the GCD of a number input by user using math package functions.
import math
number1 = int(input("enter any integer value: "))
number2 = int(input("again enter any interger value: "))
print(math.gcd(number1,number2))


#(Q.9)- Q.9- Use OS package and do the following tasks: 
#1. Get current working directory.
#2. Get the user environment.
import os
print(os.getcwd())
print(os.environ)