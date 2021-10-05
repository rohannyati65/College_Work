A="I am a human being"
B="I am good"
C="Good graders study well"
D="Humans love graders"
E="Every human does not study well"
e="Every human study well"#here e is the negation of E
print("Is every human good grader ")
truths=[[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]]
print("A","\t\t","C","\t\t","E","\t\t","e","\t\t","(A and C and e)")
for items in truths:
    if items[0]==1:
        A=False
    else: 
        A=True
    if items[1]==1:
        C=False
    else:
        C=True
    if items[2]==1:
        E=False
    else:
        E=True
    if E==True:
        e=False
    else:
        e=True
    print(A,"\t\t",C,"\t\t",E,"\t\t",e,"\t\t",(A and C and e) )
#since the result ("A and C and e" = "Is every human good garder")does not come out to be a tautology,hence every human is not a good grader)
print("every human is not a good grader")
		 
a=4**3
b=pow(4,3)
print(a,b)

int('10.8')
float(10)
int(10)
float(10.8)

print('01','Jan',sep='-',end='-2020')
x=27
y=4
print(x//y)

n_s=10
r10=10
x005=10

import sys
print(sys.version)

a=5
b=6
c=print(a/b)
type(a)

a,b,c=55
print(a)
print(b)

import array as arr
a=arr.array('d',[0,1,2,3,4,5,6,7,8,9])
print(a[5::-2])

x=(0,8,9,15,17,18)
y=slice(1,-2)
x[y]

tuple=(2,4,6,3,7)
tuple1=(1,2,3)
tuple+tuple1
len(tuple)

import numpy as np
N=np.array([24,None,29,'str',np.nan,23,30])
N.size()


M = set ([11,12,12,13,14,15])
M = {11,12,13,14}
M = set ([11,12],[13,14],[14,15])
M = set ((11,12,13,14))

s={12,13,14,15}
s.intersection_update({17,13,14,16});
print(s)

a={1,2,3}
b={4,5,6}
a^b

c={}
c[1]=1
c['1']=2
c[1]+=1
print(c)

n = [x*x for x in range(4)]
print(n)

list = [2, 4, 6, 8]
a = (x**3 for x in list)
print(next(a))

import numpy as np
np.full((3,3),True)

import copy
x=[5,4,3,2,1]
y=[7,8,9]
z=[x,y]
a=copy.deepcopy(z)
b=copy.copy(z)
x[2]=6
print('a=',a,'b=',b)
