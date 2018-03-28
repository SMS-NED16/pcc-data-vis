import pygal
from die import Die
import prod_module as prod

"""MAIN PROGRAMME BEGINS HERE"""
#Initialising Dice
die_1 = Die()
die_2 = Die()
rolls = 50000

#Getting Product of Rolling Dice
prod_results = prod.get_roll_product(die_1, die_2, rolls)

#Printing Preliminary Summary
prod.print_basic_summary(prod_results)
min_product = min(prod_results)
max_product = max(prod_results)

#Generating frequency distribution list
frequencies = prod.populate_frequencies(prod_results)

#Plotting bar chart
graph = pygal.Bar()
graph.title = "Bar char showing product of rolling two D6 dice".title()
graph.x_title = "Product"
graph.y_title = "Frequency of Product"
graph.x_labels = [str(val) for val in range(min_product, max_product + 1)]

#Adding data to bar chart and saving as svg
graph.add("D6 x D6", frequencies)
graph.render_to_file("15_9_multiplication.svg")



