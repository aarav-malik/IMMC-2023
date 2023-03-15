import pandas as pd
import statistics

total_area = 8690 #Wayne County, Cayuga County, Seneca County, Onondaga County, Oswego County
unemployment = 31815.44
unemploymentperkm = unemployment/total_area


salaries = pd.read_csv('data/salaries.csv', delimiter =',')
LPI_data = pd.read_csv('data/LPI.csv', delimiter =',')

labour =salaries[(salaries['OCC_TITLE']=="Construction Laborers")]['A_MEAN'].astype('int')

mean_labour = labour.mean(axis=0)

LPI_data["LPI"] = LPI_data['Construction Duration (years)'] * mean_labour * unemploymentperkm



print(LPI_data)