#(Q.1)- crate a list with user defined inputs. 

a = int(input("Enter first no.: "))
b = str(input("Enter second no.: "))
c = float(input("Enter third no.: "))
d = int(input("Enter fourth no.: "))
l = [a,b,c,d]
print(l)
print(type(l))

#(Q.2)- Add the following list to above created list: 
#[‘google’,’apple’,’facebook’,’microsoft’,’tesla’] 

print(l)
list = ["google,apple,facebook,microsoft,tesla"] 
print(list)
l.extend(list)
print(l)
print(type(l))

#(Q.3)- Count the number of time an object occurs in a list. 

l1 = [4,'a',4,8,'a','a']
print(l1)
print(l1.count(4))
print(type(l1))

#(Q.4)- create a list with numbers and sort it in ascending order

unsorted = [2,1,6,4,9,6]
unsorted.sort()
print(unsorted)

#(Q.5- Given are two one-dimensional arrays A and B which are sorted in ascending order.
#      Write a program to merge them into a single sorted array C that contains every item from arrays A and B,
#      in ascending order.[List] 

a = [2,3,5,7,9]
b = [0,1,4,6,8]
a.extend(b)
print(a)
c = a
c.sort()
print(c)

#Q.6-Implement a stack and queue using lists.
# push/append in stack
s=[]
print(s)
s.append(1)
s.append(2)
s.append(3
s.append(4)
print(s)

# pop from stack
s.pop()
print(s)

#OPTIONAL QUESTION
#Q.1- Count even and odd numbers in that list.
l=[3,6,5,8,1,2]
print(l)
e=0
o=0
for x in l:
    if x%2==0:
	    e=e+1
	else:
	    o=o+1
	print(e)
	print(o)

