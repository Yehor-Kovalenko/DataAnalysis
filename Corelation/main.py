import csv

import matplotlib.pyplot as plt
import numpy as np

from Calculations import pearson
from Calculations import slope_a
from Calculations import init_value_b

data = open("./data.csv")
csv.reader(data)
rows = []
for row in csv.reader(data):
    rows.append(row)
data = np.array(rows, dtype=np.float64)

def drawPlot(x1, y1):
    # dane
    x2 = []
    for x in range(len(data)):
        x2.append(data[x][x1])

    y2 = []
    for x in range(len(data)):
        y2.append(data[x][y1])

    # tworzenie linii regresji liniowej
    X = np.array(x2).reshape(-1, 1)
    plt.scatter(x2, y2)
    plt.plot(X, slope_a(x2, y2) * X + init_value_b(x2, y2), color='red')

    corr_coefficient = pearson(x2, y2)  # współczynnik pearsona

    # wyświetlenie współczynnika i równania regresji liniowej
    if init_value_b(x2, y2) > 0 :
        equation = f'y = {slope_a(x2, y2):.1f}x + {init_value_b(x2, y2):.1f}'
    else :
        equation = f'y = {slope_a(x2, y2):.1f}x - {abs(init_value_b(x2, y2)):.1f}'
    plt.title(f'r={round(corr_coefficient, 2)}; {equation}', fontsize=14)

#########################################################################################

drawPlot(0, 1)

plt.xlabel('Długość działki kielicha (cm)', fontsize=14)
plt.ylabel('Szerokość działki kielicha (cm)', fontsize=14)
plt.show()

drawPlot(0, 2)

plt.xlabel('Długość działki kielicha (cm)', fontsize=14)
plt.ylabel('Długość płatka (cm)', fontsize=14)
plt.show()

drawPlot(0, 3)

plt.xlabel('Długość działki kielicha (cm)', fontsize=14)
plt.ylabel('Szerokość płatka (cm)', fontsize=14)
plt.show()

drawPlot(1, 2)

plt.xlabel('Szerokość działki kielicha (cm)', fontsize=14)
plt.ylabel('Długość płatka (cm)', fontsize=14)
plt.show()

drawPlot(1, 3)

plt.xlabel('Szerokość działki kielicha (cm)', fontsize=14)
plt.ylabel('Szerokość płatka (cm)', fontsize=14)
plt.show()

drawPlot(2, 3)

plt.xlabel('Długość płatka (cm)', fontsize=14)
plt.ylabel('Szerokość płatka (cm)', fontsize=14)
plt.show()