import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/population.csv")
df.rename( columns={'Unnamed: 0':'Location'}, inplace=True )

for i, row in df.iterrows():
    location = row[0]
    population = row[1:]
    population = [int(p.replace(",", "")) for p in population]
    plt.plot(range(2010, 2020), population, label=location)

plt.xlabel("Year")
plt.ylabel("Population")
plt.title("Population by Location")
plt.legend()
plt.show()