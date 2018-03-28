import pygal 
from die import Die

"""Simulates and visualizes rolling three D6 dice 100000 times"""

#Create three instances of Die with 6 sides
die_1 = Die()
die_2 = Die()
die_3 = Die()

number_of_rolls = 100000

#Rolls
results = []
for roll in range(number_of_rolls):
	result = die_1.roll() + die_2.roll() + die_3.roll()
	results.append(result)

#Storing min-max results
min_result = min(results)
max_result = max(results)

#Frequency distribution
frequencies = []
for value in range(min_result, max_result + 1):
	frequency = results.count(value)
	frequencies.append(frequency)

#Creating pygal bar chart
bar_chart = pygal.Bar()
bar_chart.title = "Result of rolling three D6 dice " + str(number_of_rolls) + " times"
bar_chart.x_title = "Value"
bar_chart.y_title = "Frequency of Value"
bar_chart.x_labels = [str(val) for val in range(min_result, max_result + 1)]

bar_chart.add("Three D6", frequencies)
bar_chart.render_to_file("15_8_three_D6.svg")