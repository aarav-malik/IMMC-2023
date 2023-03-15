import pandas as pd
import numpy as np

benefits = pd.read_csv('data/Socialbenefitsdata.csv', delimiter =',')
salarys = pd.read_csv('data/Salary benefits data.csv', delimiter =',')

for benefit in benefits.iterrows():
    social_interaction_benefits = (benefits['People affected'] * benefits['Magnitude'] * benefits['Duration'])/365

benefits['Social interaction benefit score'] = social_interaction_benefits

#normalising the data


for salary in salarys.iterrows():
    salary_benefits = (salarys['People affected'] * salarys['Magnitude'] * salarys['Duration'])/365

salarys['salary benefits'] = salary_benefits
#summation function for over all social benefits (Social interaction and Job salary)
overall_social_benefits = benefits['Social interaction benefit score'] + salarys['salary benefits']



final_table = pd.DataFrame({})
final_table['Facility'] = benefits['Facilities']
final_table['Overall score'] = overall_social_benefits



for x in final_table.iterrows():
    normalised_socialbenefits = (final_table['Overall score']-np.nanmin(final_table['Overall score']))/(np.nanmax(final_table['Overall score'])-np.nanmin(final_table['Overall score']))
    final_table['Normalised Score'] = normalised_socialbenefits

print(final_table)
