# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 12:02:04 2021

@author: Rohan
"""

def linear_Search(list1, n, key):  
  
    # Searching list1 sequentially  
    for i in range(0, n):  
        if (list1[i] == key):  
            return i  
    return -1  
  
  
list1 = [10 ,30, 50, 40, 70, 90]  
key = 40  
  
n = len(list1)  
res = linear_Search(list1, n, key)  
if(res == -1):  
    print("Element not found")  
else:  
    print("Element found at index: ", res)