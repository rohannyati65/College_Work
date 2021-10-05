# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 23:56:31 2020

@author: Rohan
"""

from math import log2
import numpy as np 

def calc_entropy(class_values:list):

	total= sum(class_values)
	ys= class_values[1]
	ns= class_values[0]
	entropy= - (ys/total)*log2(ys/total) - (ns/total)*log2(ns/total)
	return entropy

def calc_informationgain(class_values:list):
    total= sum(class_values)
    yes=class_values[1]
    no=class_values[0]
    informationgain = -(yes/(total)*log2(yes/(total))) - ((no/(total))*log2(no/(total)))
    return informationgain

def calc_gain(attribute:dict, dataset_entropy:float):

	# Calculate entropy for each class in column
	entropies= {}
	for key in attribute:
		entropies[key]= calc_entropy(attribute[key])
	# Calculate total number of 1s and 0s for entire column
	total_ys= 0
	total_ns= 0
	for key in attribute:
		total_ys+= attribute[key][1]
		total_ns+= attribute[key][0]
	# 
	total= total_ys + total_ns
	# Calculates Average Weighted Entropy
	average_weighted_entropy= 0
	for key in attribute:
		average_weighted_entropy+= sum(attribute[key])/total * entropies[key]
	# Calculates Information Gain
	info_gain= dataset_entropy - average_weighted_entropy

	return info_gain


def get_max_gain(attributes:list, overall_entropy:float):

	# Calculates gain for every attribute and appends it to a list
	gains= []
	for attr in attributes:
		gain= calc_gain(attr, overall_entropy)
		gains.append(gain)

	return max(gains), gains


def calc_overall_entropy(labels:list, e=1e-8):

	class_counts= [0, 0]
	total= len(labels)
	for label in labels:
		class_counts[label]+= 1
	cls_0_ratio= class_counts[0]/total
	cls_1_ratio= class_counts[1]/total
	overall_entropy= - (cls_0_ratio*log2(cls_0_ratio+e) + cls_1_ratio*log2(cls_1_ratio+e))

	return overall_entropy


def collect_attributes(data:list, labels:list) -> list:

	attributes= []
	for column in range(len(data[0])):
		attr= {}
		for row in range(len(data)):
			k= data[row][column]
			if k not in attr:
				attr[k]= [0, 0]
			attr[k][ labels[row] ] += 1
		attributes.append(attr)

	return attributes
	

''' DATASET '''
dataset= [
	["sunny", "hot", "high", "weak"],
	["sunny", "hot", "high", "strong"],
	["overcast", "hot", "high", "weak"],
	["rain", "mild", "high", "weak"],
	["rain", "cool", "normal", "weak"],
	["rain", "cool", "normal", "strong"],
	["overcast", "cool", "normal", "strong"],
	["sunny", "mild", "high", "weak"],
	["sunny", "cool", "normal", "weak"],
	["rain", "mild", "normal", "weak"],
	["sunny", "mild", "normal", "strong"],
	["overcast", "mild", "high", "strong"],
	["overcast", "hot", "normal", "weak"],
	["rain", "mild", "high", "strong"]
]

labels= [0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0]
''''''



# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 12:36:27 2020

@author: Rohan
"""
from math import log2
import numpy as np 
import pandas as pd

data = pd.DataFrame({"toothed":["True","True","True","False","True","True","True","True","True","False"],
                     "hair":["True","True","False","True","True","True","False","False","True","False"],
                     "breathes":["True","True","True","True","True","True","False","True","True","True"],
                     "legs":["True","True","False","True","True","True","False","False","True","True"],
                     "species":["Mammal","Mammal","Reptile","Mammal","Mammal","Mammal","Reptile","Reptile","Mammal","Reptile"]}, 
                    columns=["toothed","hair","breathes","legs","species"])

features = data[["toothed","hair","breathes","legs"]]
target = data["species"]
data

def calc_informationgain(target_value:list):
    yes=target_values[1]
    no=target_values[0]
    informationgain = -(yes/(yes+no)log2(yes/(yes+no))) - ((yes/(yes+no))log2(yes/(yes+no)))
    return informationgain

def calc_entropy(target_values:list):
    total= sum(target_values)
    yes=target_values[1]
    no=target_values[0]
    entropy= - (yes/total)*log2(yes/total+e) - (no/total)*log2(no/total+e)
    return entropy
