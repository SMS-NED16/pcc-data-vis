import matplotlib.pyplot as plt

x_values = list(range(1, 1001))	
y_values = [y ** 2 for y in x_values]

#Actual plotting of the scatter plot
custom_color = (0.9, 0.5, 0.6)		#R G B between 0.0 and 1.0

plt.scatter(x_values, y_values, s=4, 
	c=y_values, edgecolor='none', cmap=plt.cm.Blues)

#Figure labelling and axes adjustment
plt.title("Scatter plot of 1000 squares".title(),fontsize=14)
plt.xlabel("Square of value", fontsize=12)
plt.ylabel("Value", fontsize=12)
plt.tick_params(axis='both', which='major')
plt.axis([0, 1100, 0, 1100 ** 2])
plt.show()
plt.savefig('squares_plot.png', bbox_inches='tight')