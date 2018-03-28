import matplotlib.pyplot as plt
from die import Die

#Creating D6 and storing results of rolling 10000 times
die_1 = Die()
total_rolls = 500000

results = []
for roll in range(total_rolls):
	results.append(die_1.roll())

frequencies = []
for value in range(min(results), max(results) + 1):
	frequency_count = results.count(value)
	frequencies.append(frequency_count)

print(frequencies)
print(sum(frequencies))

plt.figure(figsize=(10,8))
unique_values = list(set(results))
plt.plot(unique_values, frequencies, linewidth=2, marker="x",
	color="orange", markersize=10)
plt.axis([min(results) - 1, max(results) + 1, 
	min(frequencies) - total_rolls * 0.01, 
	max(frequencies) + 0.01 * total_rolls])

title_text = "Results of rolling a six-sided die " + str(total_rolls) + " times" 
plt.title(title_text.title(), fontsize=14)
plt.xlabel("Result", fontsize=12)
plt.ylabel("Frequency of result".title(), fontsize=12)
plt.legend(['D6 1'])
