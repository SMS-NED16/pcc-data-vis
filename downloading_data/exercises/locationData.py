"""A class for storing location weather data from weather underground"""
import csv
from datetime import datetime as dt

class locationData():
	def __init__(self, filename):
		self.fileName = filename
		self.highs = []
		self.lows = []
		self. dates = []
		self.readWeatherData()

	def readWeatherData(self):
		"""Opens csv file and populates highs, lows, and dates list"""
		with open(self.fileName) as f_obj:
			reader = csv.reader(f_obj)
			next(reader)
			for row in reader:
				try:
					highTemp = int(row[1])
					lowTemp = int(row[3])
					currentDate = dt.strptime(row[0], "%Y-%m-%d")
				except ValueError:
					print("Missing data for " + str(currentDate))
				else:
					self.highs.append(highTemp)
					self.lows.append(lowTemp)
					self.dates.append(currentDate)
