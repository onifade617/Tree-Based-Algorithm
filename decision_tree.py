# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 14:53:01 2025

@author: Awarri User
"""

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np


st.header("Tree Based Algorithm")


st.title("Gini Impurity")
pos_fraction = np.linspace(0.00, 1.00, 1000)

gini = 1 - (pos_fraction**2 - (1-pos_fraction)**2)


fig, ax = plt.subplots()

ax.plot(pos_fraction, gini)

ax.set_ylim(0, 1)
ax.set_xlabel('Positive fraction')

ax.set_ylabel('Gini impurity')



# Plot data
ax.plot(pos_fraction, gini, marker='o', linestyle='-')

# Set labels and limits

#ax.set_xlabel('Positive fraction')
#ax.set_ylabel('Gini impurity')
#ax.set_title('Gini Impurity vs Positive Fraction')
st.pyplot(fig)



def gini_impurity(labels):
    if len(labels) == 0:
        return 0
        counts = np.unique(labels, return_counts=True)[1]
        fractions = counts / float(len(labels))
        
    return 1 - np.sum(fractions ** 2)

st.write(f'{gini_impurity([1, 1, 0, 1, 0]):.4f}')

st.write(f'{gini_impurity([1, 1, 0, 1, 0, 0]):.4f}')

st.write(f'{gini_impurity([1, 1, 1, 1]):.4f}')