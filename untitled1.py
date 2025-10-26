# -*- coding: utf-8 -*-
"""
Created on Sun Oct 26 12:05:10 2025

@author: zemsk
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os


path = "./Alacranes Reef and Bajos del Norte reef ecological assesment"
filename_read_fish = os.path.join(path, "fish_data.csv")  # Fixed: .cvs -> .csv
filename_read_algae = os.path.join(path, "invertebrate_algae_data.csv")


df_fish = pd.read_csv(filename_read_fish)


df_algae = pd.read_csv(filename_read_algae)

print (df_algae['label'].unique())
'''
'ALG' = Algae (macroalgae, seaweed)
'INV' = Invertebrates (corals, sea urchins, sponges, etc.)
'SUB' = Substrate (non-living bottom cover like sand, rubble, rock, dead coral)
We can make data cleaner by removing SUB.
Also need to find out the difference between ALG and INV.
(does it even make sence to add ALG if its just a seaweed?)
'''



print(df_fish.columns)







