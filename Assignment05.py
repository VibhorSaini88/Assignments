#(Q.1)- Take an input year from user and decide whether it is a leap year or not.
year = int(input("enter a year: "))
if year%4==0:
	print("leap year: ",year)
else:
	print("not a leap year: ",year)
	
#(Q.2)- Take length and breadth input from user and check whether the dimensions are of square or rectangle. 
length = int(input("enter a length: "))
breadth = int(input("enter a breadth: "))
if length == breadth:
	print("dimensions are of square: ",length,breadth)
else:
	print("dimensions are of rectangle: ",length,breadth)
	
#(Q.3)- Take the input age of 3 people and determine oldest and youngest among them.
a1 = int(input("input age of first people: "))
a2 = int(input("input age of second people: "))
a3 = int(input("input age of third people: "))
if a1>a2:
	max=a1
	min=a2
else:
	max=a2
	min=a1
if a3>max:
	max=a3
else:
	if a3<min:
		min=a3
print("yonngest age: ",min)
print("oldest age: ",max)
	
#(Q.4)- Write an if statement that lets a competitor know which of these prizes they won based on the number of points they scored,
#which is stored in the integer variable points(your input). points can only take on positive integer values up to 200. 
#If they've won a prize, the message should state "Congratulations! You won a [prize name]!" with the prize name. If there's no prize, the message should state "Sorry! No prize this time."
#Points	Prize
#1-50	No Prize
#51-150	Wooden Dog
#151-180	Book
#181-200	Chocolates
point = int(input("enter any point"))
if point>=1 and point<=50:
	print("No Prize: ",point)
else:
	if point>=51 and point<=150:
		print("prize:- Wooden Dog")
	else:
		if point>=151 and point<=180:
			print("prize:- Book")
		else:
			if point>=181 and point<=200:
				print("Chocolates:-")
			else:
				print("'Sorry' for",point)

#(**Q.5- A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
#Ask user for quantity Suppose, one unit will cost 100. Judge and print total cost for user. 
quantity = int(input("enter quantity: "))
total_price = quantity*100
if total_price>1000:
	total_price = total_price - total_price*10/100

print("cost of quantity: ",total_price)

	

