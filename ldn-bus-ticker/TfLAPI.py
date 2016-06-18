import csv
import urllib2
import json

class TfLBusArrivalsAPI:
	def __init__(self):
		self.naptanDict = {}
		self.busStopDict = {}

		# row[1]     Bus stop code
		# row[2]     Naptan ID
		# row[3]     Stop name

		with open('data/tfl-bus-stops.csv') as csvfile:
		    reader = csv.reader(csvfile,delimiter=',')
		    for row in reader:
		        self.naptanDict[str(row[3])] = str(row[2])
		        self.busStopDict[str(row[1])] = str(row[2])

	def searchBusStop(self, queryString):
		"""
		Returns a list of matching bus stops to queried bus stop name, 
		and their respective Naptan IDs

		# Arugments
		queryString          String value for the bus stop name

		# Usage
		$  from TfLAPI import *
		$  tfl = TfLBusArrivalsAPI()

		$  tfl.searchBusStop('mile end')
		"""
		outputList = {}

		for busStopName, naptanID in self.naptanDict.items():
		  if queryString.upper() in str(busStopName):
		      outputList[str(busStopName)] = str(naptanID)
		  else:
		      pass
		  
		if not outputList:
		  print("No matching station found")
		  

		for busStopName, naptanID in outputList.items():
		  print("%s, %s" % (busStopName, naptanID))

	def returnTfLJSON(self, **kwargs):
		"""
		Returns a JSON style Python list containing all information
		from TfL regarding bus arrivals at specified bus stop.
		"""

		try:
			naptanID = kwargs['naptan_id']
		except KeyError:
			try:
		  		busStopCode = str(kwargs['bus_stop_code'])
		  		naptanID = self.busStopDict[str(busStopCode)]
			except KeyError:
				print("You have not specified a bus stop code (bus_stop_code='1234' or Naptan ID (naptan_id='4905N')")


		data = urllib2.urlopen("https://api.tfl.gov.uk/StopPoint/" + "%s" % naptanID + "/arrivals")
		string_data = data.read()[2:-2]
		jsonList = string_data.split('},{')

		jsonObject = []

		for element in jsonList:
			json_format = '{' + element + '}'
			jsonObject.append(json.loads(json_format))

		return jsonObject

	def queryBusArrival(self, **kwargs):
		"""
		Returns a dictionary of bus arrival times in minutes for 
		the queried bus line at the specified bus stop.

		# Arguments
		bus_line              String value for the bus line

		bus_stop_code         Integer value for the bus stop code
		### OR (not both)
		naptan_id             String value for the Naptan ID 
		                      for bus stop (obtained using searchBusStop())
		               
		# Usage
		$  from TfLAPI import *
		$  tfl = TfLBusArrivalsAPI()

		$  tfl.queryBusArrival(bus_line='205', bus_stop_code=48439)
		"""

		try:
			naptanID = kwargs['naptan_id']
		except KeyError:
			try:
		  		busStopCode = str(kwargs['bus_stop_code'])
		  		naptanID = self.busStopDict[busStopCode]
			except KeyError:
				print("You have not specified a bus stop code (bus_stop_code='1234' or Naptan ID (naptan_id='49015N')")

		try:
			busLine = kwargs['bus_line']
		except KeyError:
			print("You have not specified a bus line (bus_line='339')")

		jsonObject = self.returnTfLJSON(bus_line=kwargs['bus_line'], naptan_id=str(naptanID))
		
		busArrivalTimes = []

		for entry in jsonObject:
			if busLine in entry.values():
				arrivalMinutes = int(entry['timeToStation'])/60.0
				busArrivalTimes.append(arrivalMinutes)

		busArrivalTimes.sort()

		return busArrivalTimes
		 