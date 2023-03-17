from PI import values as PIdata
from NPV import npvs as NPVdata
from SB import final_table as SBdata
import numpy as np
import pandas as pd

final = pd.DataFrame()
PIframe = pd.DataFrame()
PIdata = np.array(sorted(PIdata))
sortedNPV = NPVdata.sort_values(by='Facilities', axis=0).reset_index()
sortedSB = SBdata.sort_values(by='Facilities', axis=0).reset_index()

final['Facilities'] = sortedNPV['Facilities']
PIframe['Facilities'] = sortedNPV['Facilities']


for i, index in enumerate(PIdata):
    PIframe.loc[i, 'Normalised Score'] = float(index.split(':')[1])

SBweight = 0.3
PIweight = 0.2
NPVweight = 0.5

print(PIframe)

final["Overall Score"] = SBweight * SBdata['Normalised Score'] + NPVweight * NPVdata["Normalised Score"]  + PIweight * PIframe["Normalised Score"] 

print("\n",final)

