# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""tuple
tuple is a collection which is ordered and unchangeable allows duplicate members."""
"""creating a tuple"""
thistuple=("apple","banana","cherry")
print(thistuple)

thistuple=("apple","banana","cherry")
print(thistuple[1])

thistuple=("apple","banana","cherry")
for x in thistuple:
    print(x)
    
thistuple=("apple","banana","cherry")
if"apple" in thistuple:
    print("yes,'apple' is in this fruits tuple")
    
thistuple=("apple","banana","cherry")
print(len(thistuple))    

thistuple=("apple","banana","cherry")
del thistuple
print(thistuple)

thistuple=tuple(("apple","banana","cherry"))
print(thistuple)

thistuple=("apple","banana","banana","cherry")
print(thistuple)
thistuple.count("banana")

"""SET"""
"""A set is a collection which is unordered and unindexed. 
In python sets are written with curly brackets."""

thisset={"apple","banana","cherry"}
print(thisset)


thisset={"apple","banana","cherry"}
for x in thisset:
    print(thisset)
    

thisset={"apple","banana","cherry"}
if "banana" in thisset:
    print("yes,'banana' is in the fruit set")    


thisset={"apple","banana","cherry"}
thisset.add("pineapple")
print(thisset)



thisset={"apple","banana","cherry"}
thisset.update(["orange","mango","grapes"])
print(thisset)

s1={1,2,3}
s2={'a','b','c'}
s1=s1.union(s2)
print(s1)


s1={1,2,3}
s2={'a','b','c'}
s1=s1.update(s2)
print(s1)


s1={1,2,3}
s2={4,2,5,6}
s1=s1.difference(s2)
print(s1)


s1={1,2,3}
s2={4,2,1,6,7}
s1=s1.intersection(s2)
print(s1)


s1={1,2,3}
s2={4,5,6}
s1=s1.isdisjoint(s2)
print(s1)


s1={1,2,3}
s2={1,2,4}
s1=s1.issubset(s2)
print(s1)


s1={1,2,3}
s2={4,5,6}
s1=s1.issuperset(s2)
print(s1)


s1={1,2,3}
s2={4,1,6}
s1=s1.difference_update(s2)
print(s1)

































    