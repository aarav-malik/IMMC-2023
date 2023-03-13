import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data/temperature.csv")
df.drop(columns=['Year'], inplace=True)
df.drop(columns=['Annual'], inplace=True)

average = df.mean()
print(average.to_numpy())

plt.plot(average.keys(), average.to_numpy())
plt.xlabel("Average of each month from 1990 to 2022")
plt.ylabel("Temperature/ºF")

plt.show()