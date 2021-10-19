import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

full_health_data = pd.read_csv("data.txt", header=0, sep=",")
# Axis of X from math
x = full_health_data["Average_Pulse"]
# Axis of Y from math
y = full_health_data["Calorie_Burnage"]

slope, intercept, r, p, std_err = stats.linregress(x, y)


def function(x1):
    return slope * x1 + intercept


myModel = list(map(function, x))

plt.scatter(x, y)
plt.plot(x, myModel)
plt.ylim(ymin=0, ymax=2000)
plt.xlim(xmin=0, xmax=200)
plt.xlabel("Average_Pulse")
plt.ylabel("Calorie_Burnage")
plt.show()
