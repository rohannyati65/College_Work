# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 12:56:09 2020

@author: Rohan
"""

"""1. Program"""

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
name = "mbox-short.txt"
handle = open(name)
text = handle.read()
words = list()
for line in handle:
    if not line.startswith("From:") : continue
    line = line.split()
    words.append(line[1])


counts = dict()

for word in words:
    counts[word] = counts.get(word, 0) + 1 

        
maxval = None
maxkey = None
for key,val in counts.items():
    if val > maxval:
        maxval = val
        maxkey = key   

print(maxkey, maxval)

"""2.program"""

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
lst=list()
for line in fh:
    if not line.startswith("From:") : 
        continue
    count = count + 1
    y=line.split()
    print(y[1])
print("There were", count, "lines in the file with From as the first word")