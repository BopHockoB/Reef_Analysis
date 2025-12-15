# -*- coding: utf-8 -*-
"""
Created on Sun Oct 26 12:05:10 2025

@author: zemsk
"""


'''
Predict reef health / ecological condition class

Define a categorical label based on cover, biomass, abundance.
'''

import matplotlib.pyplot as plt
import pandas as pd
import os


path = "../Alacranes Reef and Bajos del Norte reef ecological assesment"
filename_read_fish = os.path.join(path, "fish_data.csv")
filename_read_algae = os.path.join(path, "invertebrate_algae_data.csv")


df_fish = pd.read_csv(filename_read_fish)

'''
A_ord	Allometric constant (intercept in length–weight model)	
#Converts fish length to mass

B_pen	Allometric exponent (scaling factor in model)	
Defines growth shape and body proportion

They are fish related columns to describe their size and weight 
(remove in case enviroment prediction)
'''

df_fish_prep = df_fish.drop(['label', 'year', 'month', 'day',
              'region', 'island', 'reef', 'latitude',
              'longitude', 'habitat', 'phylum',
              'taxa1', 'taxa2', 'taxa3', 'family',
              'trophic_group','a_ord', 'b_pen',
              'id_reef','transect', 'area'], axis=1)


df_algae = pd.read_csv(filename_read_algae)



print (df_algae['label'].unique())
'''
'ALG' = Algae (macroalgae, seaweed)
'INV' = Invertebrates (corals, sea urchins, sponges, etc.)
'SUB' = Substrate (non-living bottom cover like sand, rubble, rock, dead coral)
We can make data cleaner by removing SUB.
Healthy Reef: Coral-dominated (high hard coral cover, low macroalgae)
'''

df_algae = df_algae[df_algae['label'] != "SUB"]
df_algae_prep = df_algae.drop(['label', 'year', 'month', 'day',
              'region', 'island', 'reef', 'latitude',
              'longitude', 'habitat', 'phylum',
              'taxa1', 'taxa2', 'taxa3', 'transect'],
                              axis=1)

'''
Multiple instance learning?
We need to define what has bigger influence in reef health (which dataframe to enrich)
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



ax = species_side_pivot.plot(
    kind="bar", 
    figsize=(16,6), 
    width=1,
)


plt.title("Fish Species Counts by Reef Side")
plt.xlabel("Species")
plt.ylabel("Count")
plt.xticks(rotation=90)
plt.legend(title="Reef Side")

for i in range(len(species_side_pivot)):
    ax.axvline(i - 0.5, color="lightgray", linestyle="-", linewidth=0.7)

plt.tight_layout()
plt.show()





'''
Define corellation between species presence and side protectrion status
'''

protection_status_side_count = (
    df_algae[df_algae['label'] != "SUB"]
    .groupby(["protection_status", "side"])
    .size()
    .reset_index(name="count")
    )

protection_status_fish_species = df_algae.join(other=df_fish, 
                                               on="reef_joined",
                                               how="outer",
                                               lsuffix="_algae",
                                               rsuffix="_fish")


status_fish_correlation = (
    protection_status_fish_species.groupby(["species_fish", "protection_status_algae"])
    .size()
    .reset_index(name="count")
    )

fish_trophic_map = protection_status_fish_species[["species_fish", "trophic_level_fish"]].drop_duplicates()


status_fish_correlation = status_fish_correlation.merge(
    fish_trophic_map,
    on="species_fish",
    how="left"
)


