# Author    Daniyal Ibrahim | Telematics Engineer
# Date      20.10.2020
# Python    3.7.5
from xml.dom import minidom
import pprint

import xml.etree.ElementTree as ET

def get_info(book_id):
    tree = ET.parse('books.xml')
    root = tree.getroot()
    for child in root.findall("*[@id='{0}']//".format(book_id)):
        print(child.text)

def get_xml_data():
    books_xml = minidom.parse("books.xml")
    items = books_xml.getElementsByTagName("book")
    select_one = list()
    for item in items:
        select_one.append(item.attributes['id'].value)
    return select_one

if __name__=="__main__":
    select_one=get_xml_data()
    print("___________THE LIST OF BOOKS IDS_____________")
    print(select_one)
    book_id=input("Please enter a book id: \t")
    get_info(book_id)
