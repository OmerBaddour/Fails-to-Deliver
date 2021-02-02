"""
Collect interesting entries with respect to fails-to-deliver

Source: https://www.sec.gov/data/foiadocsfailsdatahtm
"""

# filepath to data
DATA = "cnsfails202101a.txt"

# define checks
CHECKS = [
	"f2d_100000",				# 1) number of fails-to-deliver existing on the recorded day > 100,000
]


if __name__ == "__main__":
	
	# open files for each check, to write data to
	files = []
	for check in CHECKS:
		files.append(open(check + ".txt", "w"))

	# write first line of DATA to each file, since this line contains the field names
	# = "SETTLEMENT DATE|CUSIP|SYMBOL|QUANTITY (FAILS)|DESCRIPTION|PRICE"
	f_data = open(DATA, "r")
	line = f_data.readline()
	for f in files:
		f.write(line)

	# iterate over all other lines in DATA
	for line in f_data:
		parsed_line = line[:-1].split("|") # ignore trailing \n in split
		# apply each check to each entry in the data file
		for i in range(len(CHECKS)): 
			try:
				passed = False # store if line passes the current check

				if CHECKS[i] == "f2d_100000": # 1)
					if int(parsed_line[3]) > 100000:
						passed = True

				if passed: # line passed current check, write to corresponding file
					files[i].write(line)

			except Exception as e:
				print("Exception \"" + str(e) + "\" occurred with line:", line)

	# close opened files
	for f in files:
		f.close()

