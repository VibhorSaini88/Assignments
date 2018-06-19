#(Q.1)- Take 10 integers from user and print it on screen.
n = 10
i = 1
while i<=n:
	value = int(input("enter any value: "))
	print("value: ",value)
	i=i+1
print("all 10 values are printed")

#(Q.2)- Write an infinite loop.An infinite loop never ends. Condition is always true. 
n = 1
while 2:
	print("infinite loop")
	n=n+1
	
#(Q.3- Create a list of integer elements by user input. 
#Make a new list which will store square of elements of previous list.
numberList=[]
squareList=[]
n = 10
i = 1
while i<=n:
	value = int(input("enter any value: "))
	numberList.append(value)
	squareList.append(value*value)
	i=i+1
print("values enter are: ",numberList)
print("Square of values are: ",squareList)

#(Q.4)- From a list containing ints, strings and floats, make three lists to store them separately.
numberList = []
stringList = []
floatList  = []
list = [4,'string',88,20.8,'list',23.5,]
for val in list:
	if isinstance(val,int):
		numberList.append(val)
	else:
		if isinstance(val,float):
			floatList.append(val)
		else:
			stringList.append(val)
		
print("numberList is:", numberList)
print("floatList is:", floatList)
print("stringList is:", stringList)

#(Q.5)- Using range(1,101), make a list containing even and odd numbers. 
evenList = []
oddList  = []
for number in range(1,101):
	if number%2==0:
		evenList.append(number)
	else:
		oddList.append(number)
print("evenList: ",evenList)
print("oddList: ",oddList)

#(Q.6- Print the following patterns: 
# *
# **
# ***
# ****
for i in range(1,5):
	for j in range(1,i+1):
		print("*",end="")
	print()

#(Q.7)- Create a user defined dictionary and get keys corresponding to the value using for loop.
aDict={}
for i in range(1,5):
	key=input("enter any character: ")
	value=int(input("enter any int: "))
	aDict[key]=value

print(aDict)

for x in aDict:
	print(x)
	
#(Q.8- Take inputs from user to make a list. Again take one input from user and search it in the list and delete that element, 
#if found. Iterate over list using for loop.

l = []
for x in range(3):
	n = int(input("Enter a number: "))
	l.append(n)
print(l)

k = int(input("Enter the value to be deleted: "))

for x in l:
	if k == x:
		l.remove(x)

print(l)


