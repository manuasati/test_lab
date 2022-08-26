# The script looped the user to enter contacts as long as it enters y or Y.
# You must use regular expressions to validate the entries at the console. You must rerequest the question as long as the entry is invalid.
# Here are the expressions for name and  email :
# Name: ^[A-Z][a-z]+((\s|\-)[A-Z][a-z]+)?$
# Email: ^\w+[\w\-\.]*\@\w+((-\w+)|(\w*))\.[a-z]{2,4}$

# You need to create the expression for Phone number.
# When the user no longer wants to enter contacts, write the xml file containing the contacts he has entered. 
# The mycontacts.xml file must be saved in a directory named after the VLOG program.




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


def validate_name(name):
    return True if re.search("^[A-Z][a-z]+((\s|\-)[A-Z][a-z]+)?$", name) else False

def validate_email(email):
    return True if re.search("^\w+[\w\-\.]*\@\w+((-\w+)|(\w*))\.[a-z]{2,4}$", email) else False

def validate_phone(phone):
    return True if re.search("[(][\d]{3}[)][ ]?[\d]{3}-[\d]{4}", phone) else False


print ("Laboratorire par Katy")
print ("Welcome to my contact list!\n")

your_name = "VLOG" #file will be saved in this direcory
root = Element('contacts')
root.set("name", your_name)

id = 0
while True:
    while (True):
        contact_name = input ("What is the name of the contact? ")
        if validate_name(contact_name):
            break
        print ("Invalid name. ", end="")

    while (True):
        contact_phonenumber = input ("what is the contact's phone number (XXX) XXX-XXXXX? ")
        if validate_phone(contact_phonenumber):
            break
        print ("Invalid phone number. ", end="")

    while (True):
        contact_email = input ("what is the contact's email? ")
        if validate_email(contact_email):
            break
        print ("Invalid email. ", end="")

    id += 1

    contact = SubElement(root, "contact")
    contact.set("id", str(id))
    name = SubElement(contact, "name")
    name.text = contact_name
    phonenumber = SubElement(contact, "phonenumber")
    phonenumber.text = contact_phonenumber
    email = SubElement(contact, "email")
    email.text = contact_email

    another_contact = input ("Enter another contact? (y or Y): ") 
    if another_contact.strip().lower() != 'y':
        tree = ET.ElementTree(root)
        file_path = "%s/mycontacts.xml" %your_name
        create_file(file_path)
        tree.write(file_path)


        print("File Saved!\n")
        input("Pres Enter key to exit.")
        break
