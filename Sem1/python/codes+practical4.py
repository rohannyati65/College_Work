# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 10:11:53 2019

@author: 500075940
"""

a=33
b=200
if b>a:
    print("b is greater that a")
    

a=33
b=200
if b>a:
print("b is greater that a")

a=200
b=33
if b>a:
    print("b is greater than a") 
else:
    print("a is greater than b" )    
    

a=33
b=33
if b>a:
    print("b is greater than a")
elif a==b:
    print("a and b are same")
    
    
    

a=200
b=33
if b>a:
    print("b is greater than a")
elif a==b:
    print("a and b are same")
else:
    print("a is greater than b")
    
 
x=15
if x>10:
    print("above 10,")
    if x>20:
        print("and also above 20")
    else:
        print("but not above 20")
else:
    print("bye bye")
    
    
a=1
b=2
if a==1:
   if b==1:
       print("ais 1 and b is 2")
   else:
       print("bye bye")
else:
     print("bye")





'''practical 4 '''  

'''ques.1'''

x=int(input("enter a no."))
b= x%3 ==0
c= x%5 ==0
print(b,c)

'''ques.2'''
x=int(input("enter a no."))
if x%5==0:
    print("x is a multiple of 5")
else:
    print("x is not a multiple of 5")
    
'''ques.3'''
a=int(input("enter a no."))    
b=int(input("enter a no."))
c=a+b
if c>10:
    if c<20:
       print("15")
       
       
'''ques.4'''
       

a=int(input("enter a no."))
b=int(input("enter a no."))
if b>a:
    print("b is greater than a")
elif a==b:
    print("a and b are same")
else:
    print("a is greater than b")    
     
    
'''ques.5'''

x=int(input("enter your age:"))
if x>=18:
    print("voter is eligible for vote")
else:
    print("voter is not eligible for vote")
    
    
'''ques.6'''
a=int(input("enter a no."))
b=int(input("enter a no,"))
c=int(input("enter a no."))
if a>b:
   if b>c:
       if c>a:
       else:
       print("c is the largest")
   else:
       print(")