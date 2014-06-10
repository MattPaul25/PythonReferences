#internetData#
try:
    import urllib.request as urllib2
except:
    import urllib2


def webCrawl():
	#open a connection to a URL using urllib2
	webUrl = urllib2.urlopen("http://joemarini.com")
	#get the result code and print it
	print ("result code " + str(webUrl.getcode()))
	data = webUrl.read()
	print (data)

webCrawl()