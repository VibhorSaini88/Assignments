#(Q.1)- Write a program to create a tuple with different data types and do the following operations. 
# Find the length of tuples
tuple = ("tuple","false",3.2,1)
print(tuple)
print(len(tuple))

#(Q.2)-Find largest and smallest elements of a tuples. 
t=(8,9,2,7,1)
print(t)
print(max(t))
print(min(t))

#(Q.3)- Write a program to find the product of all elements of a tuple.
t=(1,2,3)
p=1
p=p*t[0]
p=p*t[1]
p=p*t[2]
print(p)

#  sets

#(Q.1)- Create two set using user defined values. 
# a. Calculate difference between two sets.
s1 = {1,2,3}
s2 = {6,2,4}
print(s1-s2)

# b. Compare two sets.
s1 = {1,2,3}
s2 = {1,4,5}
print(s1^s2)

# c. Print the result of intersection of two sets.
s1 = {1,2,3}
s2 = {1,4,5}
print(s1&s2)

# dictionary
#(Q.1)- Create a dictionary to store name and marks of 10 students by user input. 
d={}
print(d)
name=input("enter name: ")
marks=int(input("enter marks"))
d[name]= marks
name=input("enter name: ")
marks=int(input("enter marks"))
d[name]= marks
name=input("enter name: ")
marks=int(input("enter marks"))
d[name]= marks
name=input("enter name: ")
marks=int(input("enter marks"))
d[name]= marks
name=input("enter name: ")
marks=int(input("enter marks"))
d[name]= marks
name=input("enter name: ")
marks=int(input("enter marks"))
d[name]= marks
name=input("enter name: ")
marks=int(input("enter marks"))
d[name]= marks
name=input("enter name: ")
marks=int(input("enter marks"))
d[name]= marks
name=input("enter name: ")
marks=int(input("enter marks"))
d[name]= marks
name=input("enter name: ")
marks=int(input("enter marks"))

d[name] = marks
print("mydict = ",d)

#(Q.2)-Sort the dictionary created in previous question according to marks.
for key, value in sorted(d.items(), key=lambda d: d[1]):
	print ("%s: %s" % (key,value))
	

#(Q.3)- Count the number of occurrence of each letter in word "MISSISSIPPI". 
#Store count of every letter with the letter in a dictionary.
l = list("MISSISSIPPI")
d = {}
d['M'] = l.count('M')
d['I'] = l.count('I')
d['S'] = l.count('S')
d["P"] = l.count('P')
print(d)