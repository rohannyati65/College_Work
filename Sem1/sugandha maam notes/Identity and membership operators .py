# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 13:38:58 2019

@author: sugandha.sharma
"""

"""Identity Operators """
"""is  :   is 	Returns true if both variables are the
 same object"""
x = ["apple","banana"]
y = ["banana","apple"]
z = x

print(x is z) 
#returns True because z is the same object as x"""

print(x is y) 
#returns False because x is not the same object as y,even if they have the same content


print(x == y)  
#to demonstrate the difference betweeen "is" and "==": 
#this comparison returns True because x is equal to y



"""is not-  is not	Returns true if both variables
 are not the same object"""
 
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not z)

# returns False because z is the same object as x

print(x is not y)

# returns True because x is not the same object as y, even if they have the same content

print(x != y)

# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y


"""Membership Operators """
"""Membership operators are used to test if 
a sequence is presented in an object:"""
"""in 	Returns True if a sequence with the
 specified value is present in the object	"""
 
 
x = ["apple", "banana"]

print("banana" in x)

# returns True because a sequence with the
# value "banana" is in the list



x = ["apple", "banana"]

print("orange" not in x)

# returns True because a sequence 
#with the value "pineapple" is not in the list



