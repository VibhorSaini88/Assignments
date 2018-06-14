#(2).Join two string using '+'.

p = "Acad"
q = "view"
r = str(p+q)
            
print(r)
print(type(r))

#(3). Take the input of 3 variables x,y and print their value of screen. 

x = int(input("Enter first no.: "))
y = int(input("Enter second no.: "))
z = int(input("Enter third no.: "))
s = x+y+z
print(x)
print(y)
print(z)
print(s)
print(type(s))

#(4). Print "let's get started" on screen,using "\" operator.
                  
v = "let\'s get started"
print(v)
print(type(v))

q = "Hello \n World"
print(q)

p = "\'Hello\'\'world\'"
print(p)

r = "Hello \t world"
print(r)

x = 15
y = 2.5
z = 'c'
print(x,y,z,sep="-",end="!")
print("Hello World")

#(5). print the following values using "placeholder".
                    
x = 20
y = 3.5
z = 'vib'
print("%d %f %s"%(x,y,z))
print("%d+%F=%s"%(x,y,z))
print(x,"+",y,"=",z)

s      = "Acadview"
course = "Python"
fees   =  6000
print(s,"\n")
print(course,"\n")
print(type(course))
print(fees)
print(type(fees))
                   
#(6). String handling.
                 
x = "v i b h o r"
print(len(x))
                 
y = "python"
print(y.upper())
print(y.lower())				   

z = " world "
print(z.strip(),end=" ")
print("Hello")

p = "Hello"
print(p.isalpha())
                 
q = "16088"
print(q.isdigit())
                 
r = " "
print(r.isspace())
                  
s = "Python"
print(s.startswith("P"))
                    
t = "Python"
print(t.endswith("n"))

u = "world"
print(u.find("r"))
v = "Pythan"
print(v.replace("a","o"))

w = "H,E,L,o"
print(w.split(","))
				   

#(7). String word store with position(01234...)
# Eg:-    WORLD
#       +(01234)
#       -(54321)
#For(+)-> 
x ="WORLD"
print(x[1:4]) #is'ORL'
print(x[1:])  #is'ORLD'
print(x[:])   #is'WORLD'
print(x[1:100])#is'ORLD'
                   
# For(-)
print(x[-1]) #is'D'
print(x[-4]) #is'O'
print(x[:-3])#is'WO'
print(x[-3:])#is'RLD'  
                