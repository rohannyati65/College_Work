# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 11:14:51 2020

@author: Rohan
"""
"""
1.	Python Program to Print  name
2.	Python Program to Add Two Numbers
3.	Python Program to Swap Two Variables
4.	Python Program to Check if a Number is Odd or Even
5.	Python Program to Check Prime Number
6.	Python Program to Display the multiplication Table
7.	Python Program to Make a Simple Calculator
8.	Python Program to Display Fibonacci Sequence Using Recursion
9.	Python Program to Add Two Matrices
10.	Python Program to Count the Number of Each Vowel

"""
#1.	Python Program to Print  name

name=input("enter your name:")
print(name)

#2.	Python Program to Add Two Numbers

a=int(input("enter the 1st number:"))
b=int(input("enter the 2nd number:"))
print("sum of both is =", a+b)

#3.	Python Program to Swap Two Variables

x=int(input("enter the 1st number:"))
y=int(input("enter the 2nd number:"))
print("values of x & y:",x ,y)

temp=x
x=y
y=temp

print("New values of x & y:",x ,y)
   
#4.	Python Program to Check if a Number is Odd or Even

num=int(input("enter a number:"))
if num%2==0:
    print("input number is even")
    
else:
    print("input number is odd")

#5.	Python Program to Check Prime Number

num=int(input("enter the number:"))
count=0
for x in range(2,num//2):
    if num%x==0:
        count+=1
        
if count==0:
    print("the number is prime")
    
else:
    print("the number is composite")
    

#6. Python Program to Display the multiplication Table
x=int(input("enter the number: "))
for y in range(1,11):
 mult=x*y
 str="{} x {} = {}"
 print(str.format(x,y,mult)) 
 
#7. Python Program to Make a Simple Calculator
print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n")
c=input("do you want to use the calculator:")
while c=='yes' and c!='no':
 choice=int(input("What you want to do?"))
 x=int(input("1st number: "))
 y=int(input("2nd number: "))
 if choice==1:
     print("answer=", x+y)
 elif choice==2:
    print("answer=",(x-y))
 
 elif choice==3:
     print("answer=",x*y)
 elif choice==4:
     print("answer=",x/y)
 else:
     print("wrong choice!!!!")
 c=input("do you want more operations?")


#8. Python Program to Display Fibonacci Sequence Using Recursion

def fib(num):
 if num<=1:
     return num
 else:
     return fib(num-2)+fib(num-1)
num=int(input("enter the length of the series: "))
for i in range(num):
 print(fib(i),end=' ')

#9. Python Program to Add Two Matrices

import numpy as np
a=np.array([(1,2,3),(4,5,6)])
b=np.array([(1,2,3),(4,5,6)])
c= a+b
print(c)

#10.Python Program to Count the Number of Each Vowel
string=input("Enter string:")
vowels=0
for i in string:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vowels=vowels+1
print("Number of vowels are:")
print(vowels)