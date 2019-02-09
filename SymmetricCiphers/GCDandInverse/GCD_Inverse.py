# dividends = []
# remainders = []



def findgcd(a, b, multis):
	if a < b:
		return findgcd(b, a, multis)
	if a % b == 0:
		# print(b, end=" ")
		# print("is the gcd")
		return b
	else:
		# dividends.append(a)
		t = a % b
		m = int((a - t) / b)
		# remainders.append(t)
		multis.append(m)
		a = b
		b = t
		return findgcd(a, b, multis)


# quo = [15, 11, 4]
# rem = [4, 3, 1]


def invers(a, b):
	multis = []
	if a < b:
		flag = 1
	else:
		flag = 0
	if findgcd(a, b, multis) != 1:
		print ("Error : GCD not 1")
		return

	else:
		countloop = 1
		# dividends.reverse()
		# remainders.reverse()
		multis.reverse()

		d1mul = 1
		d2mul = multis[0]

		# dindex = 0
		# mindex = 0
		# rindex = 1
		noofiterations = len(multis)

		while countloop < noofiterations:
			# d1 = dividends[dindex]
			# d2 = remainders[rindex]	 #is smaller

			currentmul = multis[countloop]
			d1mulold = d1mul
			d1mul = d2mul
			d2mul = (d2mul * currentmul) + d1mulold
			countloop += 1

		print('----Answers----')
		if flag == 0:
			if (noofiterations % 2 == 0):
				
				# print('First Number (Original version) : {0}'.format(-d1mul))
				# print('First Number (Positive version) : {0}'.format(-d1mul + b))
				# print('Second Number : {0}'.format(d2mul))
				return -d1mul, -d1mul + b

			else:
				# return d1mul, -d2mul
				# print ('First Number : {0}'.format(d1mul))
				# print ('Second Number (Original version) : {0}'.format(-d2mul))							
				# print ('Second Number (Positive version) : {0}'.format(-d2mul + b))
				return d1mul - b, d1mul			
		else:
			# b = a
			if (noofiterations % 2 == 1):		
				# print ('First Number (Original version) : {0}'.format(-d2mul))			
				# print ('First Number (Positive version) : {0}'.format(-d2mul + b))
				# print ('Second Number : {0}'.format(d1mul))			
				return -d2mul, -d2mul + b

			else:
				# print ('First Number : {0}'.format(d2mul))
				# print ('Second Number (Original version) : {0}'.format(-d1mul))							
				# print ('Second Number (Positive version) : {0}'.format(-d1mul + b))			
				return d2mul, d2mul - b

if __name__ == "__main__":
    a = int(input('Enter a number : '))
    b = int(input('Enter another number : '))
    # findgcd(163, 35)
    # dividends.reverse()
    # remainders.reverse()
    # multis.reverse()
    print (invers(a, b))

    # print (dividends)
    # print (remainders)
    # print (multis)
