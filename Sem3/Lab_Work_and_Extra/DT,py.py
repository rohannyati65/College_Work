# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 12:05:22 2020

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

def entropy(target_col):
    
    elements,counts = np.unique(target_col,return_counts = True)
    entropy = np.sum([(-counts[i]/np.sum(counts))*np.log2(counts[i]/np.sum(counts)) 
    for i in range(len(elements))])
    return entropy


def InfoGain(data,split_attribute_name,target_name="class"):
   
    total_entropy = entropy(data[target_name]) 
    vals,counts= np.unique(data[split_attribute_name],return_counts=True)
    
    #Calculate the weighted entropy
    Weighted_Entropy = np.sum([(counts[i]/np.sum(counts))*entropy(data.where(data[split_attribute_name]==vals[i]).dropna()[target_name])
    for i in range(len(vals))])
    
    #Calculate the information gain
    Information_Gain = total_entropy - Weighted_Entropy
    return Information_Gain

def calc_entropy(class_values:list):
    total= sum(class_values)
    yes=class_values[1]
    no=class_values[0]
    entropy= - (yes/total)*log2(yes/total+e) - (no/total)*log2(no/total+e)
    return entropy

def calc_informationgain(class_value:list):
    yes=class_values[1]
    no=class_values[0]
    informationgain= -(yes/(yes+no)log2(yes/(yes+no)))-((yes/(yes+no))log2(yes/(yes+no)))
    return informationgain