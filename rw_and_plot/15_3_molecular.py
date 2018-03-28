import matplotlib.pyplot as plt
from random_walk import RandomWalk

"""Simulating brownian motion of a pollen grain"""

#Create a RandomWalk object and populate it with values
data_points = 5000
pollen_rw = RandomWalk(data_points)
pollen_rw.fill_walk()

#Specifying figure dimensions
plt.figure(figsize=(4.5, 4.5), dpi=150)


#Plotting random walk as a line graph instead of scatterplot
plt.plot(pollen_rw.x_values, pollen_rw.y_values, linewidth=0.5,
	color="orange")

#Plotting start and end location as scatterplot points
plt.scatter(pollen_rw.x_values[0], pollen_rw.y_values[0], 
	c='green', edgecolor='none', s=50)
plt.scatter(pollen_rw.x_values[-1], pollen_rw.y_values[-1],
	c='red', edgecolor='none', s=50)

#Figure label adjustments
plt.title("Pollen Grain in Brownian Motion")
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)
plt.show()