import csv
from matplotlib import pyplot as plt
from datetime import datetime as dt

filename = 'sitka_weather_2014.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	# Finding precipitation index - is 19
	# for index, heading in enumerate(header_row):
	# 	print(index, heading)

	dates, rainfall = [], []
	for row in reader:
		try:
			current_date = dt.strptime(row[0], "%Y-%m-%d")
			current_rain = float(row[19])
		except ValueError:
			print("Missing data for " + str(current_date))
		else:
			dates.append(current_date)
			rainfall.append(current_rain)

	#plotting
	figure = plt.figure(figsize=(10, 6), dpi=128)
	plt.plot(dates, rainfall, c="blue")
	plt.title("Rainfall in Sitka (2014", fontsize=24)
	plt.xlabel("Dates")
	plt.ylabel("Precipiation Index")
	plt.legend(['Precipitation Index'])
	plt.tick_params(axis='major', which='both')
	figure.autofmt_xdate()
	plt.show()

