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

ax.ylim(0, 1)
ax.xlabel('Positive fraction')

ax.ylabel('Gini impurity')

st.pyplot(fig)