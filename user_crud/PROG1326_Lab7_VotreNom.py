import getpass

class User(object):
	""" Defined user object.
		create user object passing params - name, city, phone  
		Args:
			name (str, mandatory): user name, to be provide during the user creation
			city (str, mandatory): user city, to be provide during the user creation
	"""
	def __init__(self, name, city, phone):
		self.name = name
		self.city = city
		self.phone = phone

	def display_name(self):
		print (self.name)

	def display_city(self):
		print (self.city)

	def display_phone(self):
		print (self.phone)

	def __str__(self):
		return "<User obj:%s>" %self.name

while(True):
	name = input ("What is your name? ")
	city = input ("%s what town do you live in ? "%name)
	phone = input ("what is your cellphone number? ")
	if name.strip() == '':
		print("name can not be empty!")
		continue
	user = User(name, city, phone)
	print ("user:", user)
	while(True):
		what_to_do = """What do you want to do ?
						1 – Print
						2 – Modification
						a – The name
						b – Town
						c – Phone number
						m – Print the menu
						3 – Print user
						4 – Exit"""
		print (what_to_do)
		command = ""
		while (True):
			command = input ("Command: ")
			if command.strip() in ["4", "m"]:
				break

			command_list = {
							"1a":user.name, 
							"1b":user.city, 
							"1c":user.phone, 
							"3":("Here is the information on the user \nName: %s \nTown: %s \nPhone %s") %(
								user.name, 
								user.city, 
								user.phone
							)
						}
			operation = command_list.get(command.strip())
			if operation:
				print (operation)
			else:
				if command.strip() == "2a":
					new_name = input ("What is your new name? : ")
					user.name = new_name
				elif command.strip() == "2b":
					new_city = input ("What is your new town? : ")
					user.city = new_city
				elif command.strip() == "2c":
					new_phone = input ("What is your new new phone number? : ")
					user.phone = new_phone
				else:
					print ("Incorrect command!")

		if command == "4":
			print ("Goodbye!")
			break

	input_key = input("Press Enter key to exit.")
	if input_key == '':
		break
