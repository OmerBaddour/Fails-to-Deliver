"""
Collect interesting statistics about fails-to-deliver

Source: https://www.sec.gov/data/foiadocsfailsdatahtm
"""

# filepath to data
DATA = "cnsfails202101a.txt"

# define statistics
STATS = [
	"total_value_by_symbol"		# 1) sum fails-to-deliver * price for each symbol
]


if __name__ == "__main__":
	
	# ignore first line of DATA (contains the field names)
	# = "SETTLEMENT DATE|CUSIP|SYMBOL|QUANTITY (FAILS)|DESCRIPTION|PRICE" 
	f_data = open(DATA, "r")
	line = f_data.readline()

	# init for each statistic
	# 1)
	symbol_to_value = dict()

	# iterate over all other lines in DATA
	for line in f_data:
		parsed_line = line[:-1].split("|") # ignore trailing \n in split
		try:

			# 1)
			if parsed_line[2] in symbol_to_value.keys():
				symbol_to_value[parsed_line[2]] += int(parsed_line[3]) * float(parsed_line[5]) 
			else:	
				symbol_to_value[parsed_line[2]] = int(parsed_line[3]) * float(parsed_line[5]) 

		except Exception as e:
			print("Exception \"" + str(e) + "\" occurred with line:", line)

	# open files for each statistic, to write data to
	files = []
	for stat in STATS:
		files.append(open(stat + ".txt", "w"))

	# write statistics to files
	# 1)
	files[0].write("SYMBOL|VALUE OF QUANTITY (FAILS) ($)\n")
	for s,v in symbol_to_value.items():
		files[0].write(s + "|" + str(round(v)) + "\n")

	# close opened files
	for f in files:
		f.close()

