# -*- coding: utf-8 -*-
"""
Created on Sun Oct 26 12:05:10 2025

@author: zemsk
"""


'''
Predict reef health / ecological condition class

Define a categorical label based on cover, biomass, abundance.
'''

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os


path = "./Alacranes Reef and Bajos del Norte reef ecological assesment"
filename_read_fish = os.path.join(path, "fish_data.csv")
filename_read_algae = os.path.join(path, "invertebrate_algae_data.csv")


df_fish = pd.read_csv(filename_read_fish)


df_algae = pd.read_csv(filename_read_algae)

print (df_algae['label'].unique())
'''
'ALG' = Algae (macroalgae, seaweed)
'INV' = Invertebrates (corals, sea urchins, sponges, etc.)
'SUB' = Substrate (non-living bottom cover like sand, rubble, rock, dead coral)
We can make data cleaner by removing SUB.
Healthy Reef: Coral-dominated (high hard coral cover, low macroalgae)
'''

algae = df_algae[df_algae['label'] == 'ALG']
invertebrate = df_algae[df_algae['label'] == 'INV']

algae_protection = algae.groupby('protection_status').size()
invertebrate_protection = invertebrate.groupby('protection_status').size()


cover_data = pd.DataFrame({
    'algae': algae_protection,
    'invertebrates': invertebrate_protection
})

'''
# Calculate percentages
comparison_pct = cover_data.div(cover_data.sum(axis=1), axis=0) * 100

comparison_pct.plot(kind='bar', stacked=True, figsize=(10, 6),
                    color=['#27ae60', '#e67e22'], edgecolor='black')
plt.xlabel('Protection Status')
plt.ylabel('Percentage (%)')
plt.title('Reef Community Composition (%) by Protection Status')
plt.axhline(y=50, color='red', linestyle='--', linewidth=1, alpha=0.7, label='50% threshold')
plt.xticks(rotation=45)
plt.legend(title='Type')
plt.tight_layout()
plt.show()
'''

cover_data['coral_algae_ratio'] = cover_data['invertebrates'] / cover_data['algae']
cover_data['percent_coral'] = (cover_data['invertebrates'] / 
                                (cover_data['invertebrates'] + cover_data['algae']) * 100)



'''
Try to find if all species shared between all sides
If they all shared between all sides then we could drop out this column
'''
species_side_counts = (
    df_fish.groupby(["species", "side"])
    .size()                               
    .reset_index(name="count")           
)
   
species_side_pivot = species_side_counts.pivot(
    index="species", columns="side", values="count"
).fillna(0)



species_side_pivot.plot(
    kind="bar", 
    figsize=(16,6), 
    width=0.8,
)

plt.title("Fish Species Counts by Reef Side")
plt.xlabel("Species")
plt.ylabel("Count")
plt.xticks(rotation=90)
plt.legend(title="Reef Side")
plt.tight_layout()
plt.show()





'''
We can drop next features:
Year, month, day, lat, long, phylum, taxa1, taxa2, taxa3, species, 

'''







