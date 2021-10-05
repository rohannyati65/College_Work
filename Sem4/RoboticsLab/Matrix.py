# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 14:33:38 2021

@author: Rohan
"""

import numpy as np 
  
# input two matrices 
Matrix1 = ([2, 4, 6],[1 ,12, 9],[5, 0, 7]) 
Matrix2 = ([3, 8, 5],[9, 1, 10],[6, 4, 8]) 
  
# This will return dot product 
Matrix3 = np.dot(Matrix1, Matrix2) 

# print resulted matrix multiplication
print("Matrix multiplication : ")
print(Matrix3) 

#python program to transpose a matrix

Matrix4 = Matrix3.transpose()
print("Transpose of a matrix : ")
print(Matrix4)

# Python program to inverse a matrix 
print("Inverse of a matrix : ")
# Calculating the inverse of the matrix 
print(np.linalg.inv(Matrix3))



