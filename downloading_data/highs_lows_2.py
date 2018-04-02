import csv
from matplotlib import pyplot as plt
from datetime import datetime


filename = 'sitka_weather_2014.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	#creating empty lists to store temps and dates
	lows, highs, dates = [], [], []
	for row in reader:
		#convert string date to datetime object in correct format
		current_date = datetime.strptime(row[0], "%Y-%m-%d")
		dates.append(current_date)

		#typecasting temperature row data to int 
		#so can be plotted with matplotlib
		highs.append(int(row[1]))

		#extracting low temperatures for plotting
		lows.append(int(row[3]))
	
	#creating figure
	fig = plt.figure(figsize=(10, 6), dpi=128)

	#creating line graph within figure
	plt.plot(dates, highs, c="red", alpha=0.8)
	plt.plot(dates, lows, c="blue", alpha=0.8)
	plt.title("Daily high and low temperatures - 2014", fontsize=24)
	plt.xlabel("", fontsize=16)
	plt.ylabel("Temperature (F)", fontsize=16)
	plt.tick_params(axis='both', which='major', labelsize=16)
	fig.autofmt_xdate()	#change formatting/angle for dates

	#filling space between high and low to show variation
	plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

	#displaying plot
	plt.show()