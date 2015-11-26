
# acount for quarters
# <30 use past previous hour
# > 30 use until next hour
# map 1 - 30

time_map = {
	1  : 'one',
	2  : 'two',
	3  : 'three',
	4  : 'four',
	5  : 'five',
	6  : 'six',
	7  : 'seven',
	8  : 'eight',
	9  : 'nine',
	10 : 'ten',
	11 : 'eleven',
	12 : 'twelve',
	13 : 'thirteen',
	14 : 'fourteen',
	15 : 'quarter',
	16 : 'sixteen',
	17 : 'seventeen',
	18 : 'eighteen',
	19 : 'nineteen',
	20 : 'twenty',
	21 : 'twentyone',
	22 : 'twentytwo',
	23 : 'twentythree',
	24 : 'twentyfour',
	25 : 'twentyfive',
	26 : 'twentysix',
	27 : 'twentyseven',
	28 : 'twentyeight',
	29 : 'twentynine',
	30 : 'half'
}

MINUTES = 60
HALF_HOUR = 30

def time_convert(string):
	time = [int(o) for o in string.split(':')]

	if time[1] > HALF_HOUR:
		minutes = MINUTES - time[1]
		hours = time[0] + 1
		if minutes != 15:
			return "{0} minutes to {1)".format(time_map[minutes], time_map[hours])
		else:
			return "{0} to {1}".format(time_map[minutes], time_map[hours])
	else:
		if time[1] != 15:
			return "{0} minutes past {1}".format(time_map[time[1]], time_map[time[0]]) if time[1] is not 1 else "{0} minute past {1}".format(time_map[time[1]], time_map[time[0]])
		else:
			return "quarter past {0}".format(time_map[time[0]])	


def main():
	print(time_convert(input()))
#end 
if __name__ == '__main__':
	main()