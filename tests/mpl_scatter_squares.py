import matplotlib.pyplot as plt

x_values = [x for x in range(1, 6)]
y_values = [y ** 2 for y in x_values]


plt.scatter(x_values, y_values, s=100)
plt.title("Scatter Plot of squares against values", fontsize=14)
plt.xlabel("Value", fontsize=12)
plt.ylabel("Square of value", fontsize=12)
plt.tick_params(axis='both', which='major', labelsize=14)
plt.show()