# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 14:35:45 2021

@author: Rohan
"""

from gekko import GEKKO
m = GEKKO()           # create GEKKO model
y = m.Var(value=2)    # define new variable, initial value=2
m.Equation(y**2==1)   # define new equation
m.options.SOLVER=1    # change solver (1=APOPT,3=IPOPT)
m.solve(disp=False)
print('y: ' + str(y.value)) # print variable value