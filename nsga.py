import numpy as np
from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.config import Config
from pymoo.core.problem import Problem
from pymoo.factory import get_problem, get_termination
from pymoo.optimize import minimize

locations = [1, 2, 3]
profits = np.array([10, 5, 8])
env_scores = np.array([8, 7, 9])
social_scores = np.array([6, 7, 5])
capacity = np.array([20, 20, 20])
Config.warnings['not_compiled'] = False

class FLP(Problem):
    def __init__(self, locations, profits, env_scores, social_scores, capacity):
        self.locations = locations
        self.profits = profits
        self.env_scores = env_scores
        self.social_scores = social_scores
        self.capacity = capacity
        self.num_locations = len(locations)

        super().__init__(
            n_var=self.num_locations,
            n_obj=3,
            n_constr=1,
            xl=0,
            xu=1
        )

    def _evaluate(self, x, out, *args, **kwargs):
        selected_locs = x.astype(bool)
        unique_locs = np.unique(np.nonzero(selected_locs)[0])
        max_index = len(self.locations) - 1
        if unique_locs[-1] > max_index:
            unique_locs = unique_locs[:max_index+1]
        total_profit = np.sum(self.profits[unique_locs][None] * selected_locs[:, None], axis=0)
        total_env_score = np.sum(self.env_scores[unique_locs][None] * selected_locs[:, None], axis=0)
        total_social_score = np.sum(self.social_scores[unique_locs][None] * selected_locs[:, None], axis=0)
        capacity_penalty = np.max(np.sum(total_social_score) - np.sum(self.capacity), 0)
        out["F"] = np.array([-total_profit, -total_env_score, total_social_score])
        out["G"] = np.array([capacity_penalty, [capacity_penalty], [capacity_penalty]])

problem = FLP(locations, profits, env_scores, social_scores, capacity)
algorithm = NSGA2(pop_size=3, crossover_prob=0.8, mutation_prob=1/3, tournament_size=3)
res = minimize(problem, algorithm, seed=1)

best_facilities = np.argsort(profits)[::-1][:2] 

print("Best facilities for profit making are: ", end="")
for i, loc in enumerate(locations):
    if i in best_facilities:
        print(loc, end=" ")
print()

import json
import random
import matplotlib.pyplot as plt

with open('data/map.json') as f:
    data = json.load(f)

fig, ax = plt.subplots()
ax.set_title('Facility Map with Selected Sites')
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
coords = data['features'][0]['geometry']['coordinates'][0]
lats, longs = zip(*coords)
ax.plot(longs, lats, color='blue')

facilities = [(random.uniform(min(longs), max(longs)), random.uniform(min(lats), max(lats)))
              for i in range(3)]

for facility in facilities:
    ax.plot(facility[0], facility[1], marker='o', markersize=10, color="red")

plt.show()
