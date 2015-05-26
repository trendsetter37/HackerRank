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
	21 : 'twenty one',
	22 : 'twenty two',
	23 : 'twenty three',
	24 : 'twenty four',
	25 : 'twenty five',
	26 : 'twenty six',
	27 : 'twenty seven',
	28 : 'twenty eight',
	29 : 'twenty nine',
	30 : 'half'
}

MINUTES = 60
HALF_HOUR = 30

def time_convert():
    time = []
    time.append(int(input()))
    time.append(int(input()))

    if time[1] > HALF_HOUR:
        minutes = MINUTES - time[1]
        hours = time[0] + 1 if time[0] != 12 else 1
        if minutes != 15:
            return "{0} minutes to {1}".format(time_map[minutes], time_map[hours])
        else:
            return "{0} to {1}".format(time_map[minutes], time_map[hours])
    elif time[1] == 0:
        return "{0} o' clock".format(time_map[time[0]])
    elif time[1] == 30:
        return "{0} past {1}".format(time_map[time[1]], time_map[time[0]])
    else:
        if time[1] != 15:
            return "{0} minutes past {1}".format(time_map[time[1]], time_map[time[0]]) if time[1] is not 1 else "{0} minute past {1}".format(time_map[time[1]], time_map[time[0]])
        else:
            return "quarter past {0}".format(time_map[time[0]])	


def main():
    print(time_convert())
#end 
if __name__ == '__main__':
    main()