import pandas as pd
import numpy as np

benefits = pd.read_csv('data/SB Data/SB(interactions).csv', delimiter =',')
salarys = pd.read_csv('data/SB Data/SB(salary).csv', delimiter =',')


for benefit in benefits.iterrows():
    social_interaction_benefits = (benefits['People affected'] * benefits['Magnitude'] * benefits['Duration'])/1000 #devided by 1000 to decrease the value down

benefits['Social interaction benefit score'] = social_interaction_benefits

#normalised salary to create a magnitude of salary ranging between 2 to 4 inclusive.
salary_magnitude = pd.read_csv('data/SB Data/SB(salary raw).csv', delimiter =',')
for value in salary_magnitude.iterrows():
    magnitude_salary = 2 + (((salary_magnitude['Salary']-np.nanmin(salary_magnitude['Salary']))*(4-2))/(np.nanmax(salary_magnitude['Salary'])-np.nanmin(salary_magnitude['Salary'])))

salarys['Magnitude'] = magnitude_salary


for salary in salarys.iterrows():
    salary_benefits = (salarys['People affected'] * (salarys['Magnitude']*salarys['Duration']))/1000 #devided by 1000 to decrease the value down

salarys['salary benefits'] = salary_benefits



#summation function for over all social benefits (Social interaction and Job salary)
overall_social_benefits = benefits['Social interaction benefit score'] + salarys['salary benefits']
print(salarys)
print(benefits)

final_table = pd.DataFrame({})
final_table['Facility'] = benefits['Facilities']
final_table['Overall score'] = overall_social_benefits


#normalised total social benefits score ranging between 1 to 10 inclusive
for x in final_table.iterrows():
    normalised_socialbenefits = ((final_table['Overall score']-np.nanmin(final_table['Overall score']))*(2-1))/(np.nanmax(final_table['Overall score'])-np.nanmin(final_table['Overall score'])) * 10
    final_table['Normalised Score'] = normalised_socialbenefits

print(final_table)