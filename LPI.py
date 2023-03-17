# Construction Cost * Unemployment% / (Area * Duration)
# Check crop farm cost, regenerative

fac = ['Sports Centre', 'Ski Facility', 'Crop Farm', 'Grazing Farm', 'Regenerative Farm', 'Agrivoltaic Farm', 'Agritourist Centre']
county = ['Wayne', 'Cayuga', 'Seneca', 'Onondaga', 'Oswego']

con_cost = [16.8, 8.35, 0.084, 0.32, 0.75, 0.079548, 0.094267]
dur = [2.5, 3, 1.15, 1.15, 1.5, 1.5, 1.5]
area = 1

# Unemployment
employed = [41300, 33700, 13900, 213800, 50100]
unemployed = [1800, 1500, 600, 8500, 2800]

labour_force = sum(employed) + sum(unemployed)
unemployed_per = sum(unemployed) / labour_force * 100

print('Old unemployment% = '+str(unemployed_per))

n=0
list_LPI=[]
sorted_LPI=[]

for x in con_cost:
    LPI = con_cost[n] * unemployed_per / (area * dur[n])
    #print(f"{fac[n]} {LPI}")
    list_LPI.append(LPI)
    sorted_LPI.append(LPI)
    n+=1
    
sorted_LPI.sort()

minimum = sorted_LPI[0]
_range = sorted_LPI[-1] - sorted_LPI[0]
#print(f'Range = {_range}')
#print(f'Minimum = {minimum}')

n=0
for x in sorted_LPI:
    normalised = (list_LPI[n] - minimum) / _range * 10
    print(f"{fac[n]} {normalised}")
    n+=1

# Assume 10% of jobs(direct and indirect) go to community
per = 0.1
jobs_direct = 9000 * per
jobs_indirect = 40000 * per
new_employed = jobs_direct + jobs_indirect + sum(employed)
new_unemployed_per = (1 - new_employed / labour_force) * 100

print('New unemployment% = '+str(new_unemployed_per))

n=0
list_LPI=[]
sorted_LPI=[]

for x in con_cost:
    LPI = con_cost[n] * new_unemployed_per / (area * dur[n])
    list_LPI.append(LPI)
    sorted_LPI.append(LPI)
    n+=1

sorted_LPI.sort()

minimum = sorted_LPI[0]
_range = sorted_LPI[-1] - sorted_LPI[0]


n=0
for x in sorted_LPI:
    normalised = 1+ ((list_LPI[n] - minimum)*9/ _range )
    print(f"{fac[n]} {normalised}")
    n+=1
