import seaborn as sns 
import matplotlib.pyplot as plt 
import numpy as np 



def gen_graph(fname):
    file1 = open(fname)
    lengths = [] 
    for line in file1: 
        line = line.split(",")
        definition = line[1] 
        words = definition.split(" ") 
        lengths.append(len(words)) 
    file1.close() 
    ax = sns.distplot(lengths) 
    sns.plt.xlabel("Lengths") 
    sns.plt.show() 

gen_graph("all_spells.csv")



