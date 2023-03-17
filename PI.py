# Construction Cost * Unemployment% / (Area * Duration)
# Check crop farm cost, regenerative

fac=['sports centre ','ski facility ','grazing farm ','regenerative farm ','agrivoltaic farm ','agritourist centre ']
county=['wayne','cayuga','seneca','onondaga','oswego']
con_cost=[32,20,0.69802,0.32,0.879546,0.094267]
dur=[2.5,3,1.15,1.15,1.5,1.5,1.5]
area=[0.5,1.5,0.809,0.809,0.809,0.00018]

# Unemployment
employed = [41300, 33700, 13900, 213800, 50100]
unemployed = [1800, 1500, 600, 8500, 2800]

labour_force = sum(employed) + sum(unemployed)
unemployed_per = sum(unemployed) / labour_force * 100
print( 'Old unemployment% (pre micron)= '+str(unemployed_per))

n=0
list_PI=[]
sorted_PI=[]

for x in con_cost:
    PI = con_cost[n] * unemployed_per / (area[n] * dur[n])
    #print(f"{fac[n]} {PI}")
    list_PI.append(PI)
    sorted_PI.append(PI)
    n+=1
    
sorted_PI.sort()

minimum = sorted_PI[0]
_range = sorted_PI[-1] - sorted_PI[0]
#print(f'Range = {_range}')
#print(f'Minimum = {minimum}')

n=0
values = []
for x in sorted_PI:
    normalised = 1+ (list_PI[n] - minimum)*9 / _range 
    values += [f"{fac[n]}:{normalised}"]
    n+=1
print(values)
# Assume 10% of jobs(direct and indirect) go to community
per = 0.1
jobs_direct = 9000 * per
jobs_indirect = 40000 * per
new_employed = jobs_direct + jobs_indirect + sum(employed)
new_unemployed_per = (1 - new_employed / labour_force) * 100
print('New unemployment% (post micron)= '+str(new_unemployed_per))

n=0
list_PI=[]
sorted_PI=[]

for x in con_cost:
    PI = con_cost[n] * new_unemployed_per / (area[n] * dur[n])
    list_PI.append(PI)
    sorted_PI.append(PI)
    n+=1

sorted_PI.sort()

minimum = sorted_PI[0]
_range = sorted_PI[-1] - sorted_PI[0]


n=0
new_values = []
for x in sorted_PI:
    normalised = 1+ ((list_PI[n] - minimum)*9/ _range )
    new_values += [f"{fac[n]}, {normalised}"]
    n+=1
print(new_values)