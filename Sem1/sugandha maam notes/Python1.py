  # -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
print("hello")  #F9 is used for interpreting a sub code at a time 




if 5>2:     #CONDITION 
 print("5 is greater than 2")
 
 
 
 
 
 X=5
 Y="JOHN"
 print(X)
 print(Y)
 
 
 
 
 
 x,y,z="orange","Banana","cherry"
 print(x)
 print(y)
 print(z)
 
 
 
 

x=y=z="orange"
print(x)
print(y)
print(z)
 



 
"""To concatenate both text and a variable of type string , 
Python uses the + operator""" 

x = "a simple programming language "
print("Python is " + x)

x = "10"
print("Python is     " + x)



"""You can also use the + operator to concatenate a string 
variable with another string variable:"""

x = "Python is "
y = "a simple programming language "
z =  x + y
print(z)





"""For numbers, the + operator works as a
 mathematical operator"""
x = 5
y = 10
print(x + y)





"""another alternative"""
x = 5
y = 10
z=x+y
print(z)






""" If you try to combine a string and a number, Python will 
give you an error:
x = 5
y = "John"
print(x + y) """

'''x = 5
y = "John"
z=x+y
print(z) '''


"""There are three numeric types in Python:
int
float
complex
Variables of numeric types are created when you assign a
 value to them:
"""

x = 1    # int
y = 2.8  # float
z = 1j   # complex

""" To verify the type of any object in Python, use the type() function:"""
print(type(x))

print(type(y))
print(type(z))





"""Int, or integer, is a whole number, positive or negative, 
without decimals, of unlimited length."""
x = 1
y = 35656222554887711
z = -3255522
print(type(x))
print(type(y))
print(type(z))





HELLO WORLD!
01234567891011




"""Strings"""
str = 'Hello World!'
print (str )       # Prints complete string
print (str[0])       # Prints first character of the string
print (str[:5])     # Prints characters starting from 3rd to 5th
print (str[2:12] )     # Prints string starting from 3rd character
print (str * 5 )     # Prints string two times
print ( str + "TEST") # Prints concatenated string

print("Upes \n" * 4)
print("upes \t" *5)
print("upes    Upes\n" *10)