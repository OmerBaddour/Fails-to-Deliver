
if __name__ == "__main__":

	# open files
	f_unsorted = open("total_value_by_symbol.txt", "r")
	f_sorted = open("sorted_tvbs.txt", "w")
	
	# write fields of f_unsorted to f_sorted
	line = f_unsorted.readline() 
	f_sorted.write(line)

	# read and sort values in f_unsorted
	s_to_v = []
	for line in f_unsorted:
		parsed = line[:-1].split("|") # ignore trailing \n
		s_to_v.append([parsed[0], int(parsed[1])])

	s_to_v = sorted(s_to_v, key = lambda x: x[1], reverse=True) 

	# write sorted values to f_sorted
	for entry in s_to_v:
		f_sorted.write(entry[0] + "|" + str(entry[1]) + "\n")

	# close files
	f_unsorted.close()
	f_sorted.close()
