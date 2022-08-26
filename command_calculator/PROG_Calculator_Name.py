# Create the class Calculator.
#The init method contains a list of numbers and total initialized to 0.0

# Create the inputNumbers method

#Request the user for positive floats as long as the user enters y or Y.
#The list must contain 2 or more numbers.
#Use the try except to validate the floats.

#Add a positive float to the list:
#Invalid number. Try again:
#Do you want to add another number? (y or Y):
#You need at least 2 numbers in the list

# Create the calculate method that takes an operation as a parameter.
#Do the operations with the list.
#Each calculates returns the total.
#The division must request a number greater than or equal to 0 (try ... except to validate).
# \ nWhich number do you want to divide by:
#Invalid number. Try again:

#Example if my list contains 3 numbers [25.0, 5.0, 2.0]
#Addition: 25.0 + 5.0 + 2.0 the function will return 32.0
#Multiplication: 25.0 * 5.0 * 2.0 the function will return 250.0
#Division: 25.0 + 5.0 + 2.0 divide by the number requested.
#Use the try except with the division for no error (ZeroDivisionError)
#If the divisor is 0 the method must return
# Can not divide by 0!

from functools import reduce

def verify_float(number):
	try:
		float(number)
	except:
		return False

	if float(number)<0:
		return False
	return True

class Calculator(object):
	"""docstring for Calculator"""
	def __init__(self):
		self.number_list = []
		self.total = 0.0

	def inputNumbers(self):
		number = None
		while True:
			if not number:
				number = input ("Add a positive float to the list: ")
			if verify_float(number):
				self.number_list.append(float(number))
				command = input ("Do you want to add another number? (y or Y): ")
				number = None
				if command == 'y' or command == 'Y':
					continue
				else:
					if len(self.number_list) < 2:
						print ("You need at least 2 numebrs in the list")
					else:
						break
			else:
				number = input("invalid number. Try again: ")

	def calcualte(self, operater):
		self.total = reduce(lambda x, y: eval( "%s%s%s" %(x, operater, y)), self.number_list)
		