# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 10:57:52 2019

@author: sugandha.sharma
"""

"""Practical No 3
Q1) Write a program to find simple interest."""

Principal = int(input('Enter Principal Amount: '))
Rate = int(input('Enter Rate Of Interest: '))
Time=int(input('Enter Time Period: '))
Simple_Interest=(Principal*Rate*Time)/100
Simple_Interest=str(Simple_Interest)
print("Simple interest is :" + Simple_Interest)


"""Q2) Write a program to find volume of cone.
Hint=(pi r**2 h)/3"""

import math
radius=10
height=10
Volume_Of_Cone=((math.pi) * radius**2 * height)/3
print(Volume_Of_Cone)


"""Q4) Write a program to convert given seconds 
into hours, minutes and remaining seconds."""


 

  
     
      

 
 
 
 
 
 
 
 
 
 
"""Q5) Write a program to convert given inches
 to feet and feet into inches format.
 Hint: 1 feet=12 inches"""
 
Feet_input=int(input("enter feet :"))
Inch_output=Feet_input*12
print("the total number of inches are :"+str(Inch_output) )
Inch_input= int(input("enter inches :"))
Feet_output= (Inch_input /12)
print("the total number of Feet are :"+str(Feet_output) )
 
 
 
"""Q6) Write a program to calculate volume of 
cylinder. Hint:pi r**2 h"""
import math
radius=10
height=10
Volume_Of_Cylinder=((math.pi) * radius**2 * height)
print(Volume_Of_Cylinder)




"""Q7) Write a program to swap two numbers without temp variable ."""
int1 = int(input("Enter first number: "))
int2 = int(input("Enter second number: "))

print('Old value of int1 is {0} and int2 is {1}'.format(int1, int2))

int1 = int1 + int2
int2 = int1 - int2
int1 = int1 - int2

# Display the result
print('New value of int1 is {0} and int2 is {1}'.format(int1, int2))









