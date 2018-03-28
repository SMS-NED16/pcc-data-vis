import matplotlib.pyplot as plt

x = list(range(1, 6))
five_cubes = [val ** 3 for val in x]
thousand_cubes = [ val ** 3 for val in range(1, 5001)]

plt.subplot(1, 2, 1)
plt.scatter(x, five_cubes, s=40)
plt.title("Graph of first five cubes", fontsize=14)
plt.xlabel("Values", fontsize=12)
plt.ylabel("Cube of Value", fontsize=12)
plt.tick_params(labelsize=12, axis='both',which='major')

plt.subplot(1, 2, 2)
x = list(range(1, 5001))
plt.scatter(x, thousand_cubes, 
	c = thousand_cubes, cmap = plt.cm.Blues, edgecolor='none',)
plt.title("Graph of five thousand cubes", fontsize=14)
plt.xlabel("Values", fontsize=12)
plt.ylabel("Cube of Values", fontsize=12)
plt.tick_params(labelsize=12, axis='both',which='major')
plt.show()