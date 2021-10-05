# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 09:04:24 2019

@author: Rohan
"""

a=int(input("enter number:"))
if(a%4==0 and a%400==0 | a%100!=0):
    print(a,"is leap year")
else:
    print("not a leap year")
    