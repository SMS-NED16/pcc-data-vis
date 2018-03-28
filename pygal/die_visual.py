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



