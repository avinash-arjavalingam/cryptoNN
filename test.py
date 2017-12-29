from urllib2 import Request, urlopen, URLError

request = Request('https://api.bitfinex.com/v2/tickers?symbols=tBTCUSD')

try:
	response = urlopen(request)
	file = response.read()
        print file
except URLError, e:
    print 'Error, pls', e