#Test par Anthony \nWelcome to my employees!\n

#\nWhat is the name of your company?
#r"^[A-Z][a-zA-Z \.,]+$
#Invalid. What is the name of your company?

#\nWhat is the name of the employee?
#Invalid. What is the name of the employee? 

#\nWhat is his/her employee number? 
#Invalid. What is his/her employee number?

#\nWhat is his salary? 
#Invalid salary. What is his/her salary?

#\nHow many hours did he work?
#Invalid. How many hours did he/she work? 

#\nEnter another employee? (Y or y): 

#\nFile Saved!

#\nPress Enter key to exit.

import os
import re
import lxml
import errno

from xml.etree.ElementTree import Element, SubElement, tostring
import xml.etree.cElementTree as ET

def create_file(file_path):
    if not os.path.exists(os.path.dirname(file_path)):
        try:
            os.makedirs(os.path.dirname(file_path))
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise


def validate_company_name(value):
    return True if re.search("^[A-Z][a-zA-Z \.,]+$", value) else False

def validate_employee_name(value):
    return True if re.search("^[A-Z][a-zA-Z \.,]+$", value) else False

def validate_emp_number(value):
    return True if re.search("^[0-9]{6}$") else False

def validate_emp_salary(value):
    return True if re.search("^[\d]{1,8}.[\d]{2}$", value) else False

def validate_emp_hours(value):
    return True if re.search("^[\d]{1,8}.[\d]{1}$", value) else False

print ("Test per Katy Mallard")
print ("Welcome to my employees!\n")


while (True):
    company = input ("What is the name of your company? ")
    if validate_company_name(company):
        break
    print ("Invalid. ", end="")

root = Element('myEmployees')
root.set("name", company)

while True:
    while (True):
        emp_name = input ("what is the name of the employee? ")
        if validate_employee_name(emp_name):
            break
        print ("Invalid. ", end="")

    while (True):
        emp_number = input ("what is his/her employee number? ")
        if validate_emp_number(emp_number):
            break
        print ("Invalid. ", end="")

    while (True):
        emp_salary = input ("what is his/her salary? ")
        if validate_emp_salary(emp_salary):
            break
        print ("Invalid. ", end="")

    while (True):
        emp_hours = input ("how many hours did he/she work? ")
        if validate_emp_hours(emp_hours):
            break
        print ("Invalid. ", end="")

    employee = SubElement(root, "employee")
    employee.set("employee-num", str(emp_number))

    name = SubElement(employee, "name")
    name.text = emp_name
    salary = SubElement(employee, "salary")
    salary.text = "%.2f" %float(emp_salary)
    hours = SubElement(employee, "hours")
    hours.text = emp_hours
    pay = SubElement(employee, "pay")
    pay.text = "%.2f" %(float(emp_salary) * float(emp_hours))

    another_contact = input ("Enter another contact? (y or Y): ") 
    if another_contact.strip().lower() != 'y':
        tree = ET.ElementTree(root)
        file_path = "%s/myEmployees.xml" %company
        create_file(file_path)
        tree.write(file_path)


        print("File Saved!\n")
        input("Pres Enter key to exit.")
        break