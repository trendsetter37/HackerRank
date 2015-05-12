from functools import reduce
import sys
import test

# From HackerRank Sh
# So far this is slow, improve
def operation(N, M, input_list):
	s=0
	for i in input_list[1::]:
		stuff = [int(o) for o in i.split()]
		s += (stuff[1]-stuff[0] + 1) * stuff[2]
	return s//int(N)
    

if __name__ == '__main__' and len(sys.argv) == 1:
	t1 = open('testcase6.txt', 'r')
	t = t1.readlines()
	ta = open('testcase6_output.txt', 'r')
	taa = ta.readlines()
	N_M = t[0]
	N = N_M.split()[0]
	M = N_M.split()[1]
	

	print(operation(N, M, t))
	t1.close()
	ta.close()

    
elif  __name__ == '__main__' and sys.argv[1].lower() == 'test':
	test.unittest.main()