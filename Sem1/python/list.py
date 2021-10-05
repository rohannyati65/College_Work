# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 10:20:46 2019

@author: 500075940
"""

x=int(input("enter a no.\n"))
a= x%7==0
b= x%5==0
c=(a and b)
if (c==1):
    print("the given no is div by 7 and mul of 5")
else:
    print("the given no is either not a mul of 5 or not div by 7")
    
    
x=int(input("enter a no:"))
if(x>=1):
    if(x<=20):
        print("x is between 1 and 20")
    else:
        print("x is not between 1 and 20")
        
        
temp=int(input("enter the temp:")) 
f=((temp*(9/5)+32))  
print(f)    
  
"""LIST"""  

""" creating a list:"""
thislist=["apple","banana","cherry"]
print(thislist)

thislist=["apple","banana","cherry"]
thislist[0]="blackcurrent"
print(thislist)

thislist=["apple","banana","cherry"]
print(thislist[4])

thislist=["apple","banana","cherry"]
for x in thislist:
    print(x)

thislist=["apple","banana","cherry"]    
if "apple" in thislist:    
    print("yes,'apple' is in fruit list")
    
    
thislist=["apple","banana","cherry"]
print(len(thislist))    


thislist=["apple","banana","cherry"]
thislist.append("orange")
print(thislist)


thislist=["apple","banana","cherry"]
thislist.insert(1,"orange")
print(thislist)

thislist=["apple","banana","cherry"]
thislist.remove("banana")
print(thislist)

thislist=["apple","banana","cherry"]
thislist.pop()
print(thislist)


list1=["1","2","3"]
list2=["4","5","6"]
list1.append(list2)
print(list1)
print(len(list1))



list1=["1","2","3"]
list2=["4","5","6"]
list1.extend(list2)
print(list1)
print(len(list1))


thislist=["apple","banana","cherry"]
del thislist[0]
print(thislist)



thislist=["apple","banana","cherry"]
del thislist
print(thislist)




thislist=["apple","banana","cherry"]
mylist=thislist.copy()
print(mylist)


x=