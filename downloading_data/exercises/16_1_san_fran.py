import csv
from matplotlib import pyplot as plt 
from datetime import datetime as dt

filename = 'san_fran_2.csv'
with open(filename) as f_obj:
	reader = csv.reader(f_obj)
	header_row = next(reader)

	#printing header_row to check column names
	# for index, heading in enumerate(header_row):
	# 	print(index, heading)

	#creating empty lists to store highTemps, lowTemps, and date
	highs, lows, dates = [], [], []

	#Reading data with try/except block 
	for row in reader:
		try:
			highTemp = int(row[1])
			lowTemp = int(row[3])
			date = dt.strptime(row[0], "%m/%d/%Y")	
		except ValueError:
			print("Missing data for" + str(date))
		else:
			highs.append(highTemp)
			lows.append(lowTemp)
			dates.append(date)

	#Creating figure to plot data
	figure = plt.figure(figsize=(10, 6), dpi=128)

	#Plotting high and low temperatures on the same figure
	plt.plot(dates, highs, c='red', alpha=0.8)
	plt.plot(dates, lows, c='blue', alpha=0.8)

	#labelling figure
	plt.title("Daily Temperatures - San Francisco, CA (2015)",
		fontsize=24)
	plt.xlabel("Dates", fontsize=16)
	plt.ylabel("Temperature F", fontsize=16)
	plt.tick_params(axis='both', which='major')
	plt.legend(['Highs', 'Lows'])

	#shading area between plots
	plt.fill_between(dates, lows, highs, facecolor='blue', alpha=0.1)

	#displaying plot
	plt.show()
