# This file generates the search queries dynamically so you don't have to manually type them in.

KEYWORDS = []
cryptos = ["iota", "bitcoin", "ethereum", "litecoin", "ripple"]
prefixes = ["how to buy ", "what is "]
suffixes = [" price", " announcements"]

for crypto in cryptos:
	for prefix in prefixes:
		KEYWORDS.append(prefix + crypto)

	for suffix in suffixes:
		KEYWORDS.append(crypto + suffix)

def printKeywords():
	print KEYWORDS

def main():
	printKeywords()

if __name__ == '__main__':
	main()
