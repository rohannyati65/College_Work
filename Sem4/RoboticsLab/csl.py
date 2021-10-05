# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 17:59:48 2021

@author: Rohan
"""

"""
sys = ss("1. -2; 3. -4", "5.; 7", "6. 8", "9.")
mag, phase, omega = bode(sys)
"""

import seaborn as sns
import scipy as sp
import matplotlib.pyplot as plt
import control as ct

fig = plt.figure()
mag, phase, omega = ct.bode_plot(pt1_w001rad, Hz=False)


