from matplotlib import pyplot as plt
from locationData import locationData

def createPlot(locationObj):
	"""Takes a locationObject and uses its member variables to generate a line graph"""
	plt.plot(locationObj.dates, locationObj.highs, c='red', alpha=0.8)
	plt.plot(locationObj.dates, locationObj.lows, c='blue', alpha=0.8)

	#Adding plot labels
	plt.xlabel("Dates")
	plt.ylabel("Temperature (F)")
	plt.title("Temperature - Sitka, Alaska")
	plt.tick_params(axis='both', which='major')
	plt.legend(['Highs', 'Lows'])

	#Filling space between high and lows to show range
	plt.fill_between(locationObj.dates, locationObj.lows, 
		locationObj.highs, facecolor='blue', alpha=0.1)

	#Rotating xlabels as workaround for autofmt
	# plt.xticks(rotation=70)


#Initialising csv location objects
sitka = locationData("sitka_weather_2014.csv")
death_valley = locationData("death_valley_2014.csv")

#Creating figure for subplots
figure = plt.figure(figsize=(10, 6), dpi=128)

#Subplot 1 - Sitka
sitka_sp = plt.subplot(2, 1, 1)
createPlot(sitka)

#Subplot 2 - Death Valley
dv_sp = plt.subplot(2, 1, 2)
createPlot(death_valley)

#Display plot
figure.subplots_adjust(hspace=0.5)
plt.show()




