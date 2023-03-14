import pandas as pd
import numpy as np

GHG_WEIGHT = 0.4
EUTRO_WEIGHT = 0.3
LAND_USE_WEIGHT = 0.2
WATER_USE_WEIGHT = 0.1

crops = pd.read_csv('data/Food_Production.csv', delimiter=',')
profits = pd.read_csv('data/foodreturns.csv', delimiter=',')
for index, crop in crops.iterrows():
    ghg_score = ((crop['Greenhouse gas emissions per 1000kcal (kgCO₂eq per 1000kcal)']-np.nanmin(crops['Greenhouse gas emissions per 1000kcal (kgCO₂eq per 1000kcal)']))/(np.nanmax(crops['Greenhouse gas emissions per 1000kcal (kgCO₂eq per 1000kcal)'])-np.nanmin(crops['Greenhouse gas emissions per 1000kcal (kgCO₂eq per 1000kcal)']))) * GHG_WEIGHT
    eutro_score = ((crop['Eutrophying emissions per 1000kcal (gPO₄eq per 1000kcal)']-np.nanmin(crops['Eutrophying emissions per 1000kcal (gPO₄eq per 1000kcal)']))/(np.nanmax(crops['Eutrophying emissions per 1000kcal (gPO₄eq per 1000kcal)'])-np.nanmin(crops['Eutrophying emissions per 1000kcal (gPO₄eq per 1000kcal)']))) * EUTRO_WEIGHT
    land_use_score = ((crop['Land use per 1000kcal (m² per 1000kcal)']-np.nanmin(crops['Land use per 1000kcal (m² per 1000kcal)']))/(np.nanmax(crops['Land use per 1000kcal (m² per 1000kcal)'])-np.nanmin(crops['Land use per 1000kcal (m² per 1000kcal)']))) * LAND_USE_WEIGHT
    water_use_score = ((crop['Scarcity-weighted water use per kilogram (liters per kilogram)']-np.nanmin(crops['Scarcity-weighted water use per kilogram (liters per kilogram)']))/(np.nanmax(crops['Scarcity-weighted water use per kilogram (liters per kilogram)'])-np.nanmin(crops['Scarcity-weighted water use per kilogram (liters per kilogram)']))) * WATER_USE_WEIGHT    
    total_score = ghg_score + eutro_score + land_use_score + water_use_score
    
    crops.at[index, 'Environmental Score'] = total_score


"""
Beef, Apples, Potatoes, Tomatoes (Shortlisted due to climate conditions and demand)
Beef, Apples, Potatoes and Tomatoes are among NYC's top produce indicating demand. However,
They are not the topmost produce as the market is usually Saturated and has a lot of competition
by the most popular produce. 
"""
selected = crops[(crops["Food product"] == "Potatoes") | (crops["Food product"] == "Tomatoes")| (crops["Food product"] == "Beef (beef herd)")| (crops["Food product"] == "Apples")]
profits['Environmental Score'] = selected.iloc[::-1].reset_index(drop=True)['Environmental Score']

ENV_WEIGHT = 0.2
PROFIT_WEIGHT = 0.8


for profit in profits.iterrows():
     profit_score = ((profits['Gross Income Per acre($)'])-np.nanmin(profits['Gross Income Per acre($)']))/(np.nanmax(profits["Gross Income Per acre($)"])-np.nanmin(profits['Gross Income Per acre($)']))
     profits['Profits'] = profit_score
     overall = 0.2*profits['Environmental Score'] + 0.8*profits['Profits']
     profits['Final Score'] = overall

print(profits)