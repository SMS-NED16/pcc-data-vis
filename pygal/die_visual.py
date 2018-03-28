import pygal

from die import Die

#Create a D6 - 6 sided die
die = Die()

#Make some rolls, and store results in a list
results = []
for roll_num in range(1000):
	result = die.roll()
	results.append(result)

#Make a set of all unique values in the results list
unique_values = set(results)

#Print max, min, and all unique values to test class is working
print("Max value in results: " + str(max(results)))
print("Min value in results: " + str(min(results)))
print("Unique values:\t" + str(unique_values))

#Analyze the results
frequencies = []
for value in range(1, die.num_sides + 1):
	frequency = results.count(value)
	frequencies.append(frequency)
print(frequencies)


#Generating a bar graph using pygal
hist = pygal.Bar()
hist.title = "Results of rolling one D6 1000 times".title()
hist.x_labels = [str(x) for x in range(1, 7)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

#Adding data to bar graph and saving to file
hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')