import getpass

import PROG1326_User_VotreNom

while(True):
	print ("\n\nLab 6 - Creating and Using Modules by Katy Mallard")
	name = input ("What is your username? ")
	if name.strip() == '':
		print("username can not be empty!")
		continue

	while(True):
		password = getpass.getpass(prompt="Create a password: ")
		if password.strip() == '':
			print("password can not be empty!")
			continue

		confirm_password = getpass.getpass(prompt="Retype your password: ")
		if password.strip() != confirm_password.strip():
			print ("The passwords are different. Restart!", end='\n\n')
		else:
			break

	user = PROG1326_User_VotreNom.User(name=name, password=password)
	print ("\nHello %s please login." %name)
	password = getpass.getpass(prompt="Password: ")
	if user.check_password(password):
		print("Authentication Successful!!", end='\n\n')
	else:
		print("Authentication fault!!", end='\n\n')

	input_key = input("Press Enter key to exit.")
	if input_key == '':
		break
