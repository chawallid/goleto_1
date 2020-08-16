import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import time

x_coordinates = []
list_tmp = []
value = []

for j in range(10):
    list_tmp.append([0])
print(list_tmp)

for j in range(10):
    value.append(np.random.random())
print(value)
x = 0


for f in range(100): 
    x_coordinates.append(x)
    for j in range(1):  
        value[j]  =  np.random.random()
        if (x == 0 ):
            list_tmp[j] = [value[j]]
        else:
            list_tmp[j].append(value[j])
        print(x_coordinates , list_tmp[j])
        plt.plot(x_coordinates, list_tmp[j])
    x += 1
    plt.show()
# plot second line

# SAMPLE.JPG