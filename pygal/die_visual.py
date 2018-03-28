from die import Die

#Create a D6 - 6 sided die
die = Die()

#Make some rolls, and store results in a list
results = []
for roll_num in range(100):
	result = die.roll()
	results.append(result)

unique_values = set(results)
print(results)
print("Max value in results: " + str(max(results)))
print("Min value in results: " + str(min(results)))
print("Unique values:\t" + str(unique_values))
