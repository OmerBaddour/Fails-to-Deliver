--------------------------------------------------------------------------------

This directory contains data from https://www.sec.gov/data/foiadocsfailsdatahtm,
and programs that extract useful data. The programs are written in Python 3.

The current data file is cnsfails202101b.txt.

--------------------------------------------------------------------------------

Usage:

$ python f2d_checks.py
$ python f2d_per_ticker.py <ticker_symbol>

To delete all outputted textfiles by Python programs except this README and the
data, in a bash shell, type:

$ find *.txt \! -name README.txt \! -name cnsfails202101a.txt -delete

--------------------------------------------------------------------------------

f2d_checks.py:

Carries out checks on the entries in the data file, and outputs files
containing entries corresponding to each check.

Check 1): number of fails-to-deliver existing on the recorded day > 100,000
	* Output in f2d_100000.txt 

--------------------------------------------------------------------------------

f2d_per_ticker.py:

Outputs a graph of the total fails-to-deliver on the listed days in the data
file, for a given ticker symbol.

--------------------------------------------------------------------------------
