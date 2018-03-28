import matplotlib.pyplot as plt
from modified_rw import ModifiedRandomWalk

#Create an instance of a modified random walk
my_rw = ModifiedRandomWalk()
my_rw.fill_walk()

#Setting figure size for plot
plt.figure(figsize=(10, 6), dpi=128)

#Scatterplot 
steps = list(range(0, len(my_rw.x_values)))
plt.scatter(my_rw.x_values, my_rw.y_values, 
	c=steps, cmap=plt.cm.Blues, s=10, edgecolor='none')

#Drawing start and endpoints
plt.scatter(my_rw.x_values[0], my_rw.y_values[0], c='green', s=100)
plt.scatter(my_rw.x_values[-1], my_rw.y_values[-1], c='red', s=100)

#Removing axes and adding title
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)
plt.title("Modified Random Walk")

#Showing final plot
plt.show()
