import PROG_Calculator_Name

calc = PROG_Calculator_Name.Calculator()
calc.inputNumbers()

def display_options():
	print ("""
		------------------------------
		Operations available
		1 - Add
		2 - Divide
		3 - Multiply
		4 - Show last total
		5 - Add numbers to the list
		6 - Print the list
		7 - Clear list
		8 - Exit""")

command = None
while True:
	if not command:
		display_options()
		command = input("Command: ")

	if command == "1":
		if calc.number_list:
			calc.calcualte('+')
			print ("The result of the Addition is %s" %calc.total)
		else:
			print ("Your list is empty!")
		command = None

	elif command == "2":
		if calc.number_list:
			number = None
			while True:
				if not number:
					number = input ("Which number do you want to divide by: ")
				if PROG_Calculator_Name.verify_float(number):
					number = float(number)
					break
				else:
					number = input("invalid number. Try again: ")

			calc.calcualte('*')
			try:
				calc.total = calc.total/number
				print ("The result of the Division is %s" %calc.total)
			except ZeroDivisionError as error:
				print ("Can not divide by 0!")
		else:
			print ("Your list is empty!")
		command = None

	elif command == "3":
		if calc.number_list:
			calc.calcualte('*')
			print ("The result of the Multiplication is %s" %calc.total)
		else:
			print ("Your list is empty!")
		command = None

	elif command == "4":
		if calc.number_list:
			print ("The last total was: %s" %calc.total)
		else:
			print ("Your list is empty!")
		command = None
	elif command == "5":
		calc.inputNumbers()
		command = None
	elif command == "6":
		if calc.number_list:
			print("Here is your list %s" %calc.number_list)
		else:
			print ("Your list is empty!")
		command = None
	elif command == "7":
		calc.number_list = []
		calc.total = 0.0
		print("The list is now empty!")
		command = None
	elif command == "8":
		break
	else:
		command = input ("Invalid Command. Try again: ")


