import csv 
from matplotlib import pyplot as plt
from datetime import datetime as dt

filename = "khi_utf.csv"
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	for index, heading in enumerate(header_row):
		print(index, heading)

	dates, temperature, rain, wind = [], [], [], []
	for row in reader:
		try:
			temp = float(row[5])
			precipitation = float(row[6])
			wind_speed = float(row[7])
			dateTimeStr = row[0] + "-" + row[1] + "-" + row[2] + " " + row[3] + ":" + row[4]
			currentDT = dt.strptime(dateTimeStr, "%Y-%m-%d %H:%M")
		except ValueError:
			print("Error converting value.")
		else:
			# dates.append(currentDate)
			temperature.append(temp)
			rain.append(precipitation)
			wind.append(wind_speed)
			dates.append(currentDT)


	# Plotting 4 subplots
	fig = plt.figure(figsize=(10,6), dpi=128)

	#Subplot 1 - Temperature
	plt.subplot(3, 1, 1)
	plt.plot(dates, temperature, c='red')
	plt.title("Temperature in Karachi")
	plt.xlabel("Dates")
	plt.ylabel("Temperature C")
	plt.legend(['Temperature'])
	plt.tick_params(axis='both', which='major')

	#Subplot 2 - Rainfall
	plt.subplot(3, 1, 2)
	plt.plot(dates, rain, c='#4682b4')
	plt.title("Rainfall in Karachi")
	plt.xlabel("Dates")
	plt.ylabel("Rainfall mm")
	plt.legend(['Rainfall'])
	plt.tick_params(axis='both', which='major')

	#Subplot 2 - Rainfall
	plt.subplot(3, 1, 3)
	plt.plot(dates, wind, c='green')
	plt.title("Wind Speed in Karachi")
	plt.xlabel("Dates")
	plt.ylabel("Wind Speed km/h")
	plt.legend(['Wind Speed'])
	plt.tick_params(axis='both', which='major')	

	fig.subplots_adjust(hspace=0.5)
	fig.autofmt_xdate()
	plt.savefig("karachi.png")
	plt.show()






