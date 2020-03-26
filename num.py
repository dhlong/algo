def gcd(a,b):
	while b != 0:
		a, b = b, a%b
	return a


def prime_sieve(n):
	is_prime = [False, False, True] + [True, False]*(n//2)
	for p in range(3, n):
		if p*p > n: 
			break
		if is_prime[p]:
			for kp in range(3*p, n+1, 2*p):
				is_prime[kp] = False

	for i in range(2, n+1):
		if is_prime[i]:
			yield  i


def miller(n):
	r = ((n-1)^(n-2)).bit_length() - 1
	d = (n-1) >> r

	def probably_prime(n, a):
		x = pow(a, d, n)
		if  x == 1 or x == n-1:
			return True
		for i in range(r-1):
			x = (x*x)%n
			if x == 1:
				return False
			if x == n-1:
				return True
		return False

	# thresholds: https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
	# wiki reference: https://www.ams.org/journals/mcom/1993-61-204/S0025-5718-1993-1192971-8/S0025-5718-1993-1192971-8.pdf
	if n < 2047:
		witnesses = [2]
	elif n < 9080191:
		witnesses = [31, 73]
	elif n < 4759123141:
		witnesses = [2, 7, 61]
	elif n < 1122004669633:
		witnesses = [2, 13, 23, 1662803]
	elif n < 2152302898747: 
		witnesses = [2, 3, 5, 7, 11]
	else:
		witnesses = [2, 3, 5, 7, 11, 13, 19, 23, 29, 31, 37] # up to 2^64

	for a in witnesses:
		if not probably_prime(n, a):
			return False

	return True


primes = [p for p in prime_sieve(1000000)]
print(primes[-10:])
for p in primes[-10:]:
	print(miller(p+2))


