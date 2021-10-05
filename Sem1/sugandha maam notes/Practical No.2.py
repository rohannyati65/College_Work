# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 09:48:00 2019

@author: sugandha.sharma
"""
"""Lab 2"""
"""
Q1) Declare these variables (x, y and z) as integers.
 Assign a value of 9 to x, Assign a value of 7 to y, 
 perform addition, multiplication, division and 
 subtraction on these two variables and
 Print out the result."""

x=9
y=7
z=str(x+y)       #Addition
print("Sum:"  + z)
z=str(x-y)       #Subtraction 
print("Difference:" + z)
z=str(x*y)       #Multiplication 
print("Product:" + z)
z=str(x/y)       #Division
print("Division :" +  z )

"""Q2)Compute the area of a square having 
side(S) equal to 145 units. Assign the result to a
 variable named area and print it."""
 
S=145
Area_Square=(S*S)
Area_Square=str(Area_Square)
print("Area of the square with side S=145 is "+ Area_Square)



""""Alternative Solution """
import math
Side=145
#number = int(input("enter a number:"))
Area_square= math.pow(Side, 2)   #power function
Area_square=str(Area_square)
print("Area Of square is :" + Area_square)



 
 """Q3) Compute the area of a triangle having base 
120 units (B) AND Height 33 units (H). Assign 
the result to a variable named area and print it."""

Base =120
Height=33
Area_Tri=1/2 *(Base*Height)    #0.5 is also acceptable 
print(Area_Tri)
 
"""Q4)Write a Program where the radius of a circle 
is 12 units. Compute the area of a circle."""

Pie=3.14
Radius=12
Area_Circle=Pie* Radius**2   #Exponent 
print(Area_Circle)


 
"""Q5)Write a Python program to solve (x+y)*(x+y)
Test data : x = 4 , y = 3
Expected output : (4+3)^2 = 49
"""

 x=4
 y=3
 z=(x+y)**2
 z=str(z)
 print("(4+3)^2="+z)
 
 
 
 """
 Q6) Write a program to compute the length of the
hypotenuse (c) of a right triangle having sides
 a = 133 , b = 72 units
. Hint : remember the Pythagoras theorem."""
 
import math
a=133 
b=72
c=math.sqrt(a**2 +b**2)   #square root function
c=str(c)
print("The length of the hypotenuse is "+ c)



"""
Q7)The user enters two numbers. Store the numbers
 in two variables called input1 and input2. 
 Swap the values of the two variables 
 so that input1 has the value of input2 and 
 vice versa. 
Print out the two variables.

"""
num1 = input('Enter First Number: ')
num2 = input('Enter Second Number: ')

print("Value of num1 before swapping: ", num1)
print("Value of num2 before swapping: ", num2)

# swapping two numbers using temporary variable
temp = num1
num1 = num2
num2 = temp

print("Value of num1 after swapping: ", num1)
print("Value of num2 after swapping: ", num2)


"""Q8) Write a python program to get the least common multiple (LCM)  of two positive integers.
Q9) Write a python program to compute the greatest common divisor  (GCD) of two positive integers.
Q10) Write a program for printing following pattern by assigning a value 1 to a variable a: 
 A)                               1
                           1      2
                     1     2      3
                1    2     3      4

B)          A
        A   A   A 
   A   A   A    A   A

 """