def baseConversion (n, base):
	conversion = "0123456789ABCDEF"
	if (base == 1):
		return (n * '1')
	elif (n < base):
		return conversion [n]
	else:
		return baseConversion(n//base,base) + conversion[n%base]

x = 1

while x == 1:
	finalValue = baseConversion (int(input('Please enter your number. ')), int(input('What base would you like to convert it to? ')))
	print (finalValue)
	repeat = input ('Would you like to convert another value? (y/n) ')
	if (repeat == 'n'):
		x = 0
