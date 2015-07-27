import math

def pfactorization(number):
	i=2
	factors = []
	n = number
	while i < math.sqrt(n)+1:
		if n%i == 0:
			n /= i 
			factors.append(i)
			
		else:
			i += 1
	if number % n == 0 or n is not 1:
		factors.append(n)
	return factors[-1] 

if __name__ == '__main__':
	T = int(raw_input())

	for i in xrange(T):
		print pfactorization(int(raw_input()))