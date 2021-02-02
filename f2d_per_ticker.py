"""
Output graph of the total fails-to-deliver on the listed days in the data, for a
given ticker symbol.

Source: https://www.sec.gov/data/foiadocsfailsdatahtm
"""

import sys
import matplotlib.pyplot as plt

# filepath to data
DATA = "cnsfails202101a.txt"


if __name__ == "__main__":
	
	# check usage
	if len(sys.argv) != 2:
		print("Incorrect usage. Should be $ python f2d_per_ticker.py <ticker_symbol>")
		exit(1)

	# check for lengthy ticker symbol
	if len(sys.argv[1]) > 10:
		print("Invalid ticker symbol. Too long. Maximum length is 10 characters.")
		exit(1)

	sys.argv[1] = sys.argv[1].upper()

	# open data
	# first line contains fields: SETTLEMENT DATE|CUSIP|SYMBOL|QUANTITY (FAILS)|DESCRIPTION|PRICE 
	f_data = open(DATA, "r")
	line = f_data.readline()

	ticker_entries = []

	# iterate over all other lines in DATA
	for line in f_data:
		parsed_line = line[:-1].split("|") # ignore trailing \n in split
		try:
			if sys.argv[1] == parsed_line[2]: 
				# ticker symbol matches that enterred on command line 
				ticker_entries.append(parsed_line)
		except Exception as e:
			print("Exception \"" + str(e) + "\" occurred with line:", line)

	# check for matches
	if len(ticker_entries) == 0:
		print("No entries with that ticker symbol found.")
		exit(1)

	# sort ticker entries by date, in case they are not sorted (though they should 
	# be) given the in-order traversal of the data.
	# fortunately the format means that casting the string representing the date
	# to an int is suffice 
	sorted(ticker_entries, key = lambda x: int(x[0]))

	# extract data
	dates = [entry[0] for entry in ticker_entries]
	f2ds = [int(entry[3]) for entry in ticker_entries]

	# plot data
	plt.plot(dates, f2ds, "k.-")
	plt.title("Failures-to-deliver for " + sys.argv[1], fontsize=20)
	plt.xlabel("Date", fontsize=16)
	plt.ylabel("Failures-to-deliver", fontsize=16)
	plt.show()

	# close opened file
	f_data.close()

