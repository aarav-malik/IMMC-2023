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
overall_socail_benefits = benefits['Social interaction benefit score'] + salarys['salary benefits']

benefits['Overall Score'] = overall_socail_benefits

print(benefits)