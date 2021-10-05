# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 11:17:43 2019

@author: Rohan
"""


x=9
y=7
z=x+y
print(z)
z=x-y
print(z)
z=x*y
print(z)
z=x/y
print(z)

s=(145)
area=(s**2)
print(area)

base=(120)
height=(33)
area=(base*height/2)
print(area)

radius=(12)
pi=(3.14)
area=(pi*(radius*radius))
print(area)

a=(133)
b=(72)
c=(((a**2)+(b**2))**(1/2))
print(c)

num1=input("enter no. 1\t")
num2=input("enter no. 2\t")
temp=num1  
num1=num2
num2=temp
print(num1,num2)

a=(4)
b=(3)
c=(((a**2)+(b**2))**(1/2))
print(c)


a=int(input("side1="))
b=int(input("side2="))
c=int(input("side3="))
s=((a+b+c)/2)
area=(s*(s-a)*(s-b)*(s-c)**(1/2))
print("area of triangle=",area)

x=4
y=3
z=(x+y)*(x+y)
print("(",x,"+",y,")","^",2,"=",z)


"""strings"""
str="helloworld!"
print(str)#prints complete string
print(str[0])#prints first character of string
print(str[12])
print(str[2:5])#prints characters starting from 3rd to 5th
print(str[9:10])#prints charaters starting from 2nd to 9th
print(str[2:])#print starting from 3rd character
print(str*2)#print starting from 2 times  
print(str*3)

print("upes\nupes\nupes\nupes\n")