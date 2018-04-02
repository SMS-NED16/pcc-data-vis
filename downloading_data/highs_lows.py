#import the csv module for reading data from csv files
import csv

#store filename of csv file as a string
filename = "sitka_weather_07-2014.csv"

#pass this string to the open function in the `with` syntax
#so that the file is opened, read, and closed automatically 
with open(filename) as f:
	#associate a reader object from the csv library with this file
	reader = csv.reader(f)

	#pass this reader object as argument to next function,
	#which will read the `next` i.e. first line of the csv file
	header_row = next(reader)

	#converting header row into an enumerate object
	#which explicitly associates each item with an index
	#this is useful because we will know which heading the 0th, 1th, 2th...nth value
	#corresponds to
	for index, column_header in enumerate(header_row):
		print(index, column_header)
