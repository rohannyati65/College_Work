print("hello") #if we press f5 it will run the entire file but if we select the line and press f9 it will only print hello


if 5>2:#condition
 print("5 is greater than 2")
 
 
X=5
Y="JOHN"
print(X) 
print(Y)


x,y,z="orange","banana","cherry"
print(x)
print(y)
print(z)


x=y=z="dehradun"
print(x)
print(y)
print(z)


x=" a simple programming language"
print("python is"+x)


"""u can also use the + operator to concatenate a string variable
 with another string variable:"""
 
 
x="python is"
y="a simple programming lang"
z=x+y
print(z)

"""for numbers,the +operator works as a mathematical operator"""

x=5
y=10
print(x+y)

#or

x=5
y=10
z=x+y
print(z)

"""if u try to combine a string and a no , python will give u error"""
x=5
y="john"
print(x+y)


#or
x=5
y="john"
z=x+y
print(z)


"""there are 3 numericals type in python:
int 
float 
complex
variables of numerical types are created when u assign a value to them"""
x=1 #int
y=2.6#float
z=1j#complex

"""to verify the type of any object in python , use the type() function"""

print(type(x))
print(type(y))
print(type(z))

"""int,is whole no , positive or negative no,without decimals,of unlimited length"""
x=1
y=982374983476932
z=-132597497
print(x)
print(y)
print(z)

"""strings"""
str='hello world!'
print(str)#prints complete string
print(str[0])#prints first character of string
#print(str[12])
print(str[2:5])#prints characters starting from 3rd to 5th
#print(str[1:9])#prints charaters starting from 2nd to 9th
print(str[2:])#print starting from 3rd character
print(str*2)#print starting from 2 times  
#print(str*3)  
print(str+"TEST")#prints concatenated string 

1.   Type conversion
you  can convert from one type to another with the int(),float(),and complex() method
  
x=2 #int
y=3.8 #float
z=5j #complex

#convert from int to float
a=float(x)

#convert from float to int:
b=int(y)

#convert from int to complex
c=complex(z)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

"""
2. random number,
python does not have a random function to make a random no , but python has a in built module


import the random module, display a random number between 1 and 9"""

import random

print(random.randrange(1,20))
print(random.uniform(10,20))

"""it returns random values within a specified range"""


'''
3. python casting:
    specify a variable type
    there may be time when u want to specify a type on to a variable
    this can be done with casting.
    python is an object oriented language,and
    as such it uses classes to define data types
    includind its primitive type
    
    casting in python is therefore done using functions:'''
    
    x=int(1) #x will be 1
    y=int(2.8) #y will be 2
    z=int("3") #z will be 3
    print(x)
    print(y)
    print(z)
    
    '''float'''
    x=float(1)#x will be 1.0
   
    y=float(2.8) # y will be 2.8
    z=float("3") #z will be 3.0
    w=float("4.2") #w will le 4.2
    print(x)
    print(y)
    print(z)
    print(w)
    
    '''strings()'''
    x=str("s1")
    y=str(2)
    z=str(3.0)
    print(x)
    print(y)
    print(z)
    
    we cannot combine strings and nos like this:
        
        #age=36
        #"my name is john,i am" +age
        #print(text)
        
        ''' but we can do so by fpllowing'''
        pi=3.14
        #text='the value of pi is' + pi ## no does not work
        text='the value of pi is' + str(pi)
        print(text) ##yes it works
        
       ''''a=6996
        text='the value of a is' + str(a)
        print(text)'''
        
        '''text code 11:
            use the format() method to insert numbers into strings'''
            
            age = 40
            txt="my name is amish , and i am {} years old"
            print(txt.format(age))
            
            '''text code 12
            
        format   method takes unlimited nos of arguments,and are placed into the respective place holders'''
            
            quantity=5
            intemno=8890
            price=199.45
            myorder="i want {} pieces of item {} for {} dollars each"
            print(myorder.format(quantity,intemno,price))
            print(myorder.format(price,quantity,intemno))
            
b="HELLO"
print(b[1:4])
print(b[1:])
print(b[:])
print(b[1:100])

s[1:100] '''is 'ello'-- an index that is too big is
 truncated down to the string length'''

''' H E L L O
    0 1 2 3 4
   -5-4-3-2-1'''
   
   b="hello"
   print(b[-1])#'last char'''
   print(b[-4])#4th char from the end'''
   print(b[:-3])#''going upto but not including the last 3 char'''
   print(b[-3:])#starting with the 3rd char from the end and extending to the end of the string'''

        
    '''text code 5'''
    a="hello,world!"
    print(len(a))
    
    '''text code 6'''
    the lowerr() method returns the string in lower case
    a="upes"
    print(a.lower())
    
    '''text code 7'''
''' upper case'''
    a="upes"
    print(a.upper())
    