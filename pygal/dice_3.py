from die import Die

import pygal

#Create a D6 and D10
die_1 = Die()
die_2 = Die(10)

#Make some rolls, and store results in a list
results = []
for roll_num in range(50000):
	result = die_1.roll() + die_2.roll()
	results.append(result)

#Storing min and max results for use in data analysis
min_result = min(results)
max_result = max(results)

#Summary of data of data
print("Unique values as a result of rolling D6 and D10")
print(set(results))
print("Minimum result:\t" + str(min_result))
print("Maximum result:\t" + str(max_result))

#Analyze the results
frequencies = []
for value in range(min_result, max_result + 1):
	frequency = results.count(value)
	frequencies.append(frequency)

#Visualize the results with a pygal bar graph
hist = pygal.Bar()
hist.title = "Results of rolling a D6 and a D10 50,000 times".title()
hist.x_labels = [str(val) for val in range(min_result, max_result + 1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D10', frequencies)
hist.render_to_file('dice_visual_3.svg')