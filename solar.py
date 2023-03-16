import csv
import matplotlib.pyplot as plt
import statistics

file_name = "data/other data/solarenergy.csv" 
 
file = open(file_name)
file_reader = csv.reader(file)
dp = list(file_reader)

# Store and remove headers from the data
headers = dp[0]
dp = dp[1:]

# The 4 locations where solar panels were installed
A, B, CDE, I = "CWSS_BLK-A", "CWSS_BLK-B", "CWSS_BLK-CDE", "CWSS_BLK-I"
# Indexing of values in each item within dp
TIMEDATE, DP_LOCATION, DP_ENERGY = 0, 1, 2
# Indexing of values in each item within processed_dp
TIME, DAY, MONTH, LOCATION, ENERGY = 0, 1, 2, 3, 4
 
# Handling data types
processed_dp = []
for i in range(len(dp)):
    dp[i][DP_ENERGY] = float(dp[i][DP_ENERGY])
    dnt = dp[i][TIMEDATE].split()
    date, time = dnt[0], dnt[1]
    date = date.split("/")
    day = int(date[0])
    month = int(date[1])
    time = time.split(":")
    time = int(time[0])
    processed_dp.append([time, day, month] + dp[i][1:])

# UDF to filter data
def filter_lst(subject, subject_value, lst):
    result = []
    for i in range(len(lst)):
        if lst[i][subject] == subject_value:
            result.append(lst[i])
    return result
    
# Filter data by locations
dp_A = filter_lst(LOCATION, A, processed_dp)
dp_B = filter_lst(LOCATION, B, processed_dp)
dp_CDE = filter_lst(LOCATION, CDE, processed_dp)
dp_I = filter_lst(LOCATION, I, processed_dp)


# UDF to retrieve the energy generated per hour
def hourly_energy_generated(lst):
    hourly_energy_per_day = []
    for month in range(lst[0][MONTH], lst[-1][MONTH]+1):
        dp_mth = filter_lst(MONTH, month, lst)
        for day in range(dp_mth[0][DAY], dp_mth[-1][DAY]+1):
            dp_day = filter_lst(DAY, day, dp_mth)
            hourly_energy = []
            for dataset in dp_day:
                hourly_energy.append(dataset[ENERGY])
            hourly_energy_per_day.append(hourly_energy)
    return hourly_energy_per_day
 
 
# UDF to calculate the total energy generated per day
def total_energy(lst):
    result = []
    for dataset in lst:
        result.append(sum(dataset))
    return result

# Retrieve maximum and total energy generated by location per day
A_hourly = hourly_energy_generated(dp_A)
A_total = total_energy(A_hourly)
B_hourly = hourly_energy_generated(dp_B)
B_total = total_energy(B_hourly)
CDE_hourly = hourly_energy_generated(dp_CDE)
CDE_total = total_energy(CDE_hourly)
I_hourly = hourly_energy_generated(dp_I)
I_total = total_energy(I_hourly)

DAILYAVERAGE_total = [(A_total[i] + B_total[i] + CDE_total[i]+ I_total[i]) / 4 for i in range(len(A_total))]
o_average = statistics.mean(DAILYAVERAGE_total)
# Plotting Graphs of Maximum Energy (kW) against Days
# Setting up x-axis values
x_total = []
for i in range(len(A_total)):
    x_total.append(i+1)
print(o_average)
# Plotting a line for each location
plt.plot(x_total, A_total, color="r", linewidth=1, label="A")
plt.plot(x_total, B_total, color="b", linewidth=1, label="B")
plt.plot(x_total, CDE_total, color="c", linewidth=1, label="CDE")
plt.plot(x_total, I_total, color="m", linewidth=1, label="I")
plt.plot(x_total, DAILYAVERAGE_total, color="k", linewidth=1, label="Daily Average")
plt.axhline(y=o_average, color="y", linewidth=1, label="Average")



plt.legend(loc = 4)
plt.title("Total Energy against Days", fontsize="14")
plt.xlabel("Days", fontsize="12")
plt.ylabel("kW", fontsize="12")
plt.show()