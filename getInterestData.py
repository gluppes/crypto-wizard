from pytrends.request import TrendReq
import keywords

kw_list = keywords.KEYWORDS
plotOn = False
allDates = {}
allInterests = {}

pytrends = TrendReq(hl='en-US', tz=360)
for kw in kw_list:
	pytrends.build_payload([kw], cat=0, timeframe='today 3-m', geo='', gprop='')

	stuff = pytrends.interest_over_time();

	if kw in stuff:
		data = stuff[kw]

		stuffToPlot = []
		for individualPairs in data.iteritems():
			stuffToPlot.append(individualPairs)

		dates, interests = zip(*stuffToPlot)


		if plotOn:
			from matplotlib import pyplot as plt
			plt.plot(dates, interests)
			plt.ylim([0, 110])
			plt.title('Search Interest for the Query \"' + kw + '\" Over the Last 90 Days')
			plt.xlabel('Date')
			plt.ylabel('Search Interest')
			plt.show()


		allDates[kw] = dates
		allInterests[kw] = interests
