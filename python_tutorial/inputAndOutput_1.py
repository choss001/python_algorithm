
def test(s):
	print(s)
	year = 2016
	event = 'Referendum'
	f'Results of the {year} {event}'

	yes_votes = 42_572_654
	no_votes = 43_132_495
	percentage = yes_votes / (yes_votes + no_votes)
	'{:-9} YES votes {:2.2%}'.format(yes_votes, percentage)

if __name__ == "__main__":
	import sys
	test(sys.argv[1])
	