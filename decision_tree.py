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


ax.set_xlabel('Positive fraction')

ax.set_ylabel('Gini impurity')



# Plot data
ax.plot(pos_fraction, gini)
ax.set_ylim(0, 1)
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
st.write("Moderately Heterogeneous")
st.write(f'{gini_impurity([1, 1, 0, 1, 0]):.4f}')

st.write("Highly Heterogeneous")
st.write(f'{gini_impurity([1, 1, 0, 1, 0, 0]):.4f}')

st.write("Highly Homogeneous")
st.write(f'{gini_impurity([1, 1, 1, 1]):.4f}')


st.title("Entropy")
pos_fraction = np.linspace(0.001, 0.999, 1000)
ent = -(pos_fraction * np.log2(pos_fraction) + (1 - pos_fraction) * np.log2(1 - pos_fraction))

fig1, ax1 = plt.subplots()
ax1.plot(pos_fraction, ent)
ax1.set_xlabel('Positive fraction')
ax1.set_ylabel('Entropy')
ax1.set_ylim(0, 1)
st.pyplot(fig1)

def entropy(labels):
    if len(labels) == 0:
        return 0
    counts = np.unique(labels, return_counts=True)[1]
    fractions = counts / float(len(labels))
    return - np.sum(fractions * np.log2(fractions))

st.write("low entropy")
st.write(f'{entropy([1, 1, 0, 1, 0]):.4f}')

st.write("high entropy")
st.write(f'{entropy([1, 1, 0, 1, 0, 0]):.4f}')

st.write("negative entropy")
st.write(f'{entropy([1, 1, 1, 1]):.4f}')