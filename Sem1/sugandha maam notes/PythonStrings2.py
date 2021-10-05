# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 10:17:08 2019

@author: sugandha.sharma
"""
'''Test code :1
String literals in python are surrounded by either single
 quotation marks, or double quotation marks.'''

x="Hello"
y='Hello'
print(x)
print(y)
print("upes")
print('upes')


'''Strings are Arrays
Like many other popular programming languages, strings in
 Python are arrays of bytes representing unicode characters.

However, Python does not have a character data type, 
a single character is simply a string with a length of 1. 
Square brackets can be used to access elements of the string.'''

'''Test code 2:
    Get the character at position 1 
(remember that the first character has the position 0)'''

a = "Hello, World!"
print(a[1])

'''Test Code 3:
    Substring. 
•	s[1:4] is 'ell' -- chars starting at index 1 and 
    extending up to but not including index 4
•	s[1:] is 'ello' -- omitting either index defaults 
    to the start or end of the string
•	s[:] is 'Hello' -- omitting both always gives 
us a copy of the whole thing 
(this is the pythonic way to copy a sequence like a 
string or list)
•	s[1:100] is 'ello' -- an index that is too big is 
truncated down to the string length
:'''
    
b = "Hello"
#print(b[1:3]) 
#print(b[2:])
#print(b[:])
print(b[2:100])

'''
•	s[-1] is 'o' -- last char (1st from the end)
•	s[-4] is 'e' -- 4th from the end
•	s[:-4] is 'H' -- going up to but not including the
 last 4 chars.
•	s[-4:] is 'ello' -- starting with the 3rd char from 
the end and extending to the end of the string.
'''
b = "Hello"
print(b[-1]) 
print(b[-4])
print(b[:-4])
print(b[-4:])


'''Test Code 4:
    The strip() method removes any whitespace 
    from the beginning or the end:'''
    
a = " Hello, World! "
b='    upes    '
print(a.strip()) 
print(b.strip())


'''Test Code 5:
The len() function returns the length of a string:'''

a = "  Hello,World!  "
print(len(a))  

  

'''Test code 6:
    The lower() method returns the string in lower case:'''
    
a = "UPES"
print(a.lower())



'''Test code 7:
    The upper() method returns the string in upper case:'''
a = "upes"
print(a.upper()) 

   
'''Test code 8:
    The replace() method replaces a string with another string:'''

a = "Hello, World,Hello UPES!"
b="UPES"
print(a.replace("He", "Ja"))
print(b.replace("U", "S"))


'''Test Code 9:
    The split() method splits the string into substrings
    if it finds instances of the separator:'''
    
a = "Hello, World!It is a beautiful day "
print(a.split("l")) # returns ['Hello', ' World!It is a beautiful day ']
print(a.split("!"))

'''Test code 10:
   We cannot combine strings and numbers like this:
    '''
#age = 36
#txt = "My name is John, I am " + age
#print(txt)
''' But you can do so by the following code '''
pi = 3.14
  ##text = 'The value of pi is ' + pi      ## NO, does not work
text = 'The value of pi is '  + str(pi)  
print(text)## yes

'''
String Format :
we can combine strings and numbers by using the 
format() method.

The format() method takes the passed arguments, formats
 them, and places
 them in the string where the placeholders {} are:'''
 
'''Test Code 11:
Use the format() method to insert numbers into strings:'''

age = 40
txt = "My name is Amish, and I am {} years old "
print(txt.format(age)) 

'''Test Code 12:
The format() method takes unlimited number of arguments, 
and are placed into the respective placeholders: '''

quantity = 5
itemno = 8890
price = 199.45
myorder = "I want {} pieces of item {} for {} Rupees each."
print(myorder.format(quantity, itemno,price))

'''Test Code 13:
You can use index numbers {0} to be sure the arguments
 are placed in the correct placeholders:
'''

quantity = 10
itemno = 100
price = 20
myorder = "I want to pay {2} Rupees each for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))



'''Test Code 14:
Check String
To check if a certain phrase or character is present in a 
string,we can use the keywords in or not in.
It returns value True or False .
It is case sensitive '''

txt = "Dehradoon is a valley in uttarakhand ."
x = "doon" in txt
y="Doon" in txt 
print(x)
print(y)

'''Test Code 15:
    
 Check if the phrase "Doon" is NOT present in the string.
 Returns Bollean value True or False .
 Case sensitive. '''

txt = "Dehradoon is a valley in uttarakhand"
x = "Doon" not in txt
print(x) 


'''Test Code 16:
   Concatenating two strings :  '''
   
a = "Hello"
b = "World"
c = a + b
print(c)
 
'''Test Code 17:
 To add a space between two strings , add a " ":'''

a = "Hello"
b = "World"
c = a + " " + b
print(c)


"""Test Code 18: Next line """
print("My name is " + "Sugandha" )
print("My name is \n"+" \n Sugandha ")

print("My name is "+"\n \tSugandha ")
x="Sugandha"
y="\tSugandha"
z=" Sugandha"
print(x)
print(y)
print(z)
print(len(x))
print(len(y))
print(len(z))



 
 
 

 
 

