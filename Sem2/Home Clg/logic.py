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
		 