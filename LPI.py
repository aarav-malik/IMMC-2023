import pandas as pd
import statistics

total_area = 141300 #Wayne County, Cayuga County, Seneca County, Onondaga County, Oswego County
unemployment = 413287
unemploymentperkm = unemployment/total_area


salaries = pd.read_csv('data/Economic Data/salaries.csv', delimiter =',')
LPI_data = pd.read_csv('data/LPI.csv', delimiter =',')

labour =salaries[(salaries['OCC_TITLE']=="Construction Laborers")]['A_MEAN'].astype('int')

mean_labour = labour.mean(axis=0)

LPI_data["LPI"] = LPI_data['Construction Duration (years)'] * mean_labour * unemploymentperkm



print(LPI_data)