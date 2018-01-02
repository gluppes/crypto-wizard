from pytrends.request import TrendReq
from matplotlib import pyplot as plt
import sys

q = sys.argv[1]

pytrends = TrendReq(hl='en-US', tz=360)
kw_list = [q]
pytrends.build_payload(kw_list, cat=0, timeframe='today 3-m', geo='', gprop='')

stuff = pytrends.interest_over_time();

data = stuff[kw_list[0]]

stuffToPlot = []
for individualPairs in data.iteritems():
	stuffToPlot.append(individualPairs)

a, b = zip(*stuffToPlot)



plt.plot(a,b)
plt.ylim([0, 110])
plt.title('Search Interest for the Query \"' + kw_list[0] + '\" Over the Last 90 Days')
plt.xlabel('Date')
plt.ylabel('Search Interest')
plt.show()