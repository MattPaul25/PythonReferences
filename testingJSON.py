import urllib2
import json

def printResults(data):
	theJSON = json.loads(data)
	if "title" in theJSON["metadata"]:
		print (theJSON["title"])

def main():
	#define a variable to hold the source URL
	# in this case we'll use the free data feed from the USGS
	#This feed lists all earthquakes for the last day larger than Mag 2.5

	urlData ="http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

	#open the url and read the data 
	WebUrl = urllib2.urlopen(urlData)
	print (WebUrl.getcode())
	if (WebUrl.getcode() == 200):
		data = WebUrl.read()
		printResults(data)
	else:
		print ("Received an error from server, cannot retrieve results " + str(WebUrl.getcode()))

if __name__ == '__main__':
	main()
