import pandas as pd
import numpy as np

npvs = pd.read_csv('data/NPV.csv', delimiter =',')

for npv in npvs.iterrows():
    present_value_for_year_1 = npvs['future present value for year 1']/(1 + npvs['expected annual return rate'])**1
    present_value_for_year_2 = npvs['future present value for year 1']/(1 + npvs['expected annual return rate'])**2
    present_value_for_year_3 = npvs['future present value for year 1']/(1 + npvs['expected annual return rate'])**3
    present_value_for_year_4 = npvs['future present value for year 1']/(1 + npvs['expected annual return rate'])**4
    present_value_for_year_5 = npvs['future present value for year 1']/(1 + npvs['expected annual return rate'])**5
    total_present_value = present_value_for_year_1 + present_value_for_year_2 + present_value_for_year_3 + present_value_for_year_4 + present_value_for_year_5

net_present_value = total_present_value - npvs['initial invested value']

npvs['net present value'] = net_present_value

print(npvs)