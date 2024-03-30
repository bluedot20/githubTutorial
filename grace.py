def digitChecker(n): 
	lDigit = n % 10 
	fDigit = n // 10 ** (digitCount(n) - 1)
	if lDigit != fDigit: 
		return False 
	return True 

def digitCount(n): 
	count = 0
	while n > 0: 
		n //= 10 
		count += 1
	return count 

def sandwich(n): 
	if digitChecker(n) == False: 
		return False 
	digit = n % 10 
	n //= 10 
	while n > 9: 
		if n % 10 == digit: 
			return False 
		n //= 10 
	return True 

print(sandwich(7117))


def nthSandwich(n):

	number = 10 
	count = -1 
	while count < n : 
		number += 1  
		if sandwich(number) == True: 
			count += 1 
	return number, count 

print(nthSandwich(1000))




def isPrime(n):
	for i in range(2, n):
		if n % i == 0: 
			return False
		return True

def testIsPrime(): 
	print("testing isPrime...")
	assert(isPrime(2) == 3)
	assert(isPrime(10) == 29)
	assert(isPrime(1) == 2)


# testIsPrime()









