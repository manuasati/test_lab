from employee import HR

print ("Devoir 4 Anthony Ilunga")
print ("Utilisation de classe et module. Script pour manipuler des employé(e)s).\n")


hr_direcotory = HR(name='directory')

while(True):
	command = "\n-------------------------------------------\n"
	command += "1 - Add employees to the directory\n"
	command += "2 - Display employee salary\n"
	command += "3 - Display employee age\n"
	command += "4 - Display all employees\n"
	command += "5 - Quit\n"
	command += "Input a command: "
	command = input (command)

	if command.strip() == "1":
		while True:
			hr_direcotory.add_employee()
			more_employee = input ("Do you want to enter another employee? (y or Y) ")
			if more_employee.strip() != "y":
				break

	elif command.strip() == "2":
		hr_direcotory.display_employee_salary()
	elif command.strip() == "3":
		hr_direcotory.return_employee_age()
	elif command.strip() == "4":
		hr_direcotory.display_all_employees()
	elif command == "5":
			break			
	else:
		print("Invalid command.\n")
input("Press Enter key to exit.")