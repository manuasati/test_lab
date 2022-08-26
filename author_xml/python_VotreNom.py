#Get 1 by Katy Mallard \ nWelcome to my library! \ N


#Regular Expression for the title: ^ [A-Za-z0-9 \ s \ -,] + $
# \ nWhat is the title of the book?
#Invalid title. What is the title of the book?

#Regular Expression for the author name: ^ [A-Z] [a-zA-Z0-9] + ([_ -]? [A-zA-Z0-9]) * $
#Who is the author?
#Invalid name. Who is the author?

#What year was it published?
#Invalid Year. What year was it published?

#What is the price of the book?
#Invalid price. What is the price of the book?

#Enter another book? (Y or y):
#File Saved!
# \ nPress Enter key to exit.


import os
import re
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


def validate_title(title):
    return True if re.search("^[A-Za-z0-9\\s\\-,]+$", title) else False

def validate_author(author):
    return True if re.search("^[A-Za-z0-9\\s\\-,]+$", author) else False

def validate_year(year):
    if year and year.isdigit():
        if int(year) >=1900 and int(year) <=2018:
            return True
    return False

def validate_price(price):
    try:
        if len(price.split('.')) !=2 or (not price.split('.')[1]): 
          return False
        price = float(price)
    except:
        return False
    return True

print ("Devoir 1 par Katy Mallard")
print ("Welcome to my library!\n")

your_name = "Katy Malland"
root = Element('library')
root.set("name", your_name)

id = 0
while True:
    while (True):
        book_title = input ("What is the title of the book? ")
        if validate_title(book_title):
            break
        print ("Invalid title. ", end="")

    while (True):
        author_name = input ("Who is the author? ")
        if validate_author(author_name):
            break
        print ("Invalid author. ", end="")

    while (True):
        pub_year = input ("What year was it published? ")
        if validate_year(pub_year):
            break
        print ("Invalid year. ", end="")

    while (True):
        book_price = input ("What is the price of the book? ")
        if validate_price(book_price):
            break
        print ("Invalid price. ", end="")

    id += 1

    book = SubElement(root, "book")
    book.set("id", str(id))
    title = SubElement(book, "title")
    title.text = book_title
    author = SubElement(book, "author")
    author.text = author_name
    year = SubElement(book, "year")
    year.text = pub_year
    price = SubElement(book, "price")
    price.text = book_price

    another_book = input ("Enter another book? (y or Y): ") 
    if another_book.strip().lower() != 'y':
        tree = ET.ElementTree(root)
        file_path = "%s/mylibrary.xml" %your_name
        create_file(file_path)
        tree.write(file_path)


        print("File Saved!\n")
        input("Pres Enter key to exit.")
        break
