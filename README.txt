--------------------------------------------------------------------------------

This directory contains data from https://www.sec.gov/data/foiadocsfailsdatahtm,
and programs that extract useful data.

The current data file is cnsfails202101a.txt.

To delete all outputted textfiles by Python programs except this README and the
data, in a bash shell, type:
$ find *.txt \! -name README.txt \! -name cnsfails202101a.txt -delete

--------------------------------------------------------------------------------

f2d_checks.py:

Outputs f2d_100000.txt and value_f2d_1000000.txt

f2d_100000.txt: Entries in the data file which have more than 100,000 fails-to-
deliver.

value_f2d_1000000.txt: Entries in the data file which have more than 1,000,000
dollars worth of value (roughly - see link for precise meaning) in fails-to-
deliver.

--------------------------------------------------------------------------------

f2d_stats.py:

Outputs total_value_by_symbol.txt: Sum of fails-to-deliver * value, for each
symbol (since there are multiple entries in the original data per symbol)

--------------------------------------------------------------------------------

sort_tvbs.py

Outputs sorted_tvbs.txt: Sorted total_value_by_symbol.txt by value.

--------------------------------------------------------------------------------
