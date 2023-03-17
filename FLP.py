import pandas as pd
import numpy as np
from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.config import Config
from pymoo.core.problem import Problem
from pymoo.optimize import minimize
from pymoo.termination import get_termination
import json
import matplotlib.pyplot as plt
Config.warnings['not_compiled'] = False

def locationnum(locations):
    if "agritourist centre" in locations or "cross country skiing facility" in locations:   # these take up 2 locations
        return list(range(1,4))
    else:
        return list(range(1,4))

                                                #1           #2          #3
datadict = {
    'cross country skiing facility': {'NPV':  np.array([7.354295,7.354295,7.354295*1.2]), 'SB_scores': np.array([84.1/10,43.8/10,75/10])},
    'outdoor sport complex': {'NPV': np.array([10.000000,10.000000,10.000000]), 'SB_scores': np.array([84.1/10,43.8/10,75/10])},
    'regenerative farm': {'NPV': np.array([5.605695*1.2,5.605695*1.2,5.605695*0.8]), 'SB_scores': np.array([84.1/10,43.8/10,75/10])},
    'agrivoltaic farm': {'NPV': np.array([5.520988*1.2,5.520988*1.2,5.520988*0.8]), 'SB_scores': np.array([84.1/10,43.8/10,75/10])},
    'grazing farm': {'NPV': np.array([5.578704,5.578704,5.578704]), 'SB_scores': np.array([84.1/10,43.8/10,75/10])},
    'agritourist centre': {'NPV': np.array([1.000000,1.000000*1.2,1.000000*0.8]), 'SB_scores': np.array([84.1/10,43.8/10,75/10])}
}

# data = pd.DataFrame.from_dict(data=datadict, orient='index')
locations = input("Input 3 facilities(separated by commas, no spaces. If F = skiing or agritourist then enter the same F twice) \n Enter Here: ")

location_ids = locationnum(locations)
class FLP(Problem):

    def __init__(self, datadict, locations, location_ids):
        #self.data = data
        self.locations = locations
        self.location_ids = location_ids
        self.datadict = datadict

        super().__init__(
            n_var=len(location_ids),
            n_obj=2,
            n_constr=0,
            xl=0,
            xu=1
        )

    def _evaluate(self, x, out, *args, **kwargs):
        selected_locs = np.round(x).astype(int)
        unique_locs = np.unique(selected_locs)
        if 0 in unique_locs:
            unique_locs = unique_locs[1:]

    # Iterate over different locations and calculate their objective function values
        NPV_per_location = []
        SB_scores_per_location = []

        for i, loc in enumerate(self.locations.split(',')):
            loc_idx = self.location_ids[i] - 1

            loc_NPV = datadict[loc]['NPV']
            loc_SB_scores = datadict[loc]['SB_scores']

            mask = (selected_locs == self.location_ids[i])
            profit_value = -np.sum(loc_NPV[mask[loc_idx]])
            SB_score_value = -np.sum(loc_SB_scores[mask[loc_idx]])


            NPV_per_location.append(profit_value)
            SB_scores_per_location.append(SB_score_value)

        out["F"] = np.column_stack([NPV_per_location, SB_scores_per_location])


 

problem = FLP(datadict, locations, location_ids)
algorithm = NSGA2(pop_size=len(location_ids), crossover_prob=0.8, mutation_prob=1/3, tournament_size=len(location_ids))
res = minimize(problem, algorithm, termination=('n_gen', 100), seed=1)


for i, loc in enumerate(locations.split(',')):
    loc_idx = location_ids[i] - 1
    selected_locs = res.X[loc_idx]

    # Print the name of the location
    print(f"\nInput {i+1} Facility: {loc}\n")

    # Iterate over different locations and print the selected locations
    for j, sel_loc in enumerate(selected_locs):
        if sel_loc > 0:
            print(f"Selected Location {j+1}: {sel_loc}")

###'''
from pymoo.indicators.hv import HV

ref_point = np.array([1.2, 1.2])

ind = HV(ref_point=ref_point)


from pymoo.visualization.scatter import Scatter

problem = FLP(datadict, locations, location_ids)

# Define the parameters to be varied
n_variations = 10
param_name = 'crossover_prob'
param_values = np.linspace(0.1, 1.0, n_variations)

# Run the optimization with varying parameter values
results = []
for value in param_values:
    algorithm = NSGA2(pop_size=len(location_ids), crossover_prob=value, mutation_prob=1/3, tournament_size=len(location_ids))
    res = minimize(problem, algorithm, termination=('n_gen', 100), seed=1)
    results.append(res)

# Extract the objective values
NPV = []
SB_scores = []
for res in results:
    NPV.append(res.F[:,0])
    SB_scores.append(res.F[:,1])

# Plot the results
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

ax1.set_title("Sensitivity Analysis for Crossover Probability")
ax1.set_xlabel(param_name)
ax1.set_ylabel("Profit")
ax1.plot(param_values, NPV, 'o-')

ax2.set_title("Sensitivity Analysis for Crossover Probability")
ax2.set_xlabel(param_name)
ax2.set_ylabel("Social Score")
ax2.plot(param_values, SB_scores, 'o-')

plt.show()

with open('data/map.json') as f:
    data = json.load(f)

fig, ax = plt.subplots()
ax.set_title('Facility Map with Selected Sites')
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
coords = data['features'][0]['geometry']['coordinates'][0]
lats, longs = zip(*coords)
ax.plot(longs, lats, color='blue')

facilities = [(43.226727, -76.689821, 'Location 1'), (43.237822, -76.694381, 'Location 2'), (43.22976624916421, -76.7061705481701, 'Location 3')]

for facility in facilities:
    ax.plot(facility[0], facility[1], marker='o', markersize=10, color="red") 
    ax.text(facility[0] + 0.002, facility[1] + 0.002, facility[2])

plt.show()


print("HV", ind(res.F))
### '''