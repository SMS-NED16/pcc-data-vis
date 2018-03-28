import pygal
from die import Die

"""Creating visualization of rolling 2 D8s"""
#Creating two D8s
die_1 = Die(8)
die_2 = Die(8)

#Setting rolls 
rolls = 1000

#Rolling dice and storing results
results = []
for roll in range(rolls):
	result = die_1.roll() + die_2.roll()
	results.append(result)

#Creating frequency distribution
frequencies = []
min_result = min(results)
max_result = max(results)

for value in range(min_result, max_result + 1):
	frequency = results.count(value)
	frequencies.append(frequency)

#Creating pygal bar chart
bar_chart = pygal.Bar()
bar_chart.title = "Result of rolling two D8 dice " + str(rolls) + " times"
bar_chart.x_labels = [str(val) for val in range(min_result, max_result + 1)]
bar_chart.x_title = "Result"
bar_chart.y_title ="Frequency of Result"

bar_chart.add("D8 + D8", frequencies)
bar_chart.render_to_file("15_7.svg")