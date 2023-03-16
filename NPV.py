import pandas as pd
import numpy as np

npvs = pd.read_csv('data/data for npv/NPV.csv', delimiter =',')
expected_annual_return_rate = (npvs['profits']/(npvs['revenue']-npvs['profits']))
npvs['expected annual return rate'] = expected_annual_return_rate

for y in npvs.iterrows():
    npvs['future present value'] = npvs['revenue']-npvs['maintenance cost']

for npv in npvs.iterrows():
    present_value_for_year_1 = npvs['future present value']/(1 + npvs['expected annual return rate'])**1
    present_value_for_year_2 = npvs['future present value']/(1 + npvs['expected annual return rate'])**2
    present_value_for_year_3 = npvs['future present value']/(1 + npvs['expected annual return rate'])**3
    present_value_for_year_4 = npvs['future present value']/(1 + npvs['expected annual return rate'])**4
    present_value_for_year_5 = npvs['future present value']/(1 + npvs['expected annual return rate'])**5
    
    npvs['Total present value'] = present_value_for_year_1 + present_value_for_year_2 + present_value_for_year_3 + present_value_for_year_4 + present_value_for_year_5

#grazing farm often lost first year benefits
npvs.at[5,'Total present value'] = ((npvs.iloc[5,7])*(4/5))

net_present_value = npvs['Total present value'] - npvs['initial invested value']
npvs['net present value'] = net_present_value

#skiing facilities can only operate 1 quarter of the year
npvs.at[0,'net present value'] = ((npvs.iloc[0,8])/4)


for x in npvs.iterrows():
    normalised_net_present_value = 1 + (((npvs['net present value']-np.nanmin(npvs['net present value']))*(9))/(np.nanmax(npvs['net present value'])-np.nanmin(npvs['net present value'])))
    npvs['Normalised Score'] = normalised_net_present_value
print(npvs)