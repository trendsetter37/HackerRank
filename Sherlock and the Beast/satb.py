#!/usr/bin/python3.4
''' Sherlock and the Beast on HackerRank '''

import sys
from colorama import Back, Style, Fore


def decent(n):
	n = int(n)
	if n == 1:
		return -1
	else:
		if n % 3 == 0:
			return '5' * n
		else:	
			for i in range(n, -1, -5): # This should return the largest
				if i % 3 == 0 and (n-i) % 5 == 0:
					return '5'*i + '3'*(n-i)
			else:
				return -1


if __name__ == '__main__':
	if len(sys.argv) < 2:
		# Will use sample testcases by default
		f = open('sample_testcase.txt', 'r')

		# testnumber case was stripped
		input_lines = f.readlines()[1::] # Each line is in a list
		g = open('sample_testcase_answers.txt', 'r')

		output_lines = g.readlines()

		for i in range(len(input_lines)):
			result = decent(input_lines[i])

			if int(result) == int(output_lines[i]):
				print(Fore.GREEN + "Testcase {} passed".format(i+1) + Style.RESET_ALL)
			else:
				print(Fore.RED + "Testcase {} failed -- Correct: {}\tActual: {}".format(i+1,\
					output_lines[i], result) + Style.RESET_ALL)

		f.close, g.close()
