# Python basics

# Author    Daniyal Ibrahim | Telematics Engineer
# Date      20.10.2020
# Python    3.7.5

"""
In this script, the basic elements and concepts of the programming language Python
sketched. For more detailed information, please refer to the 
Tutorials referred.

Online Editor: https://repl.it/languages/python3
"""

""" Comments
    ... this is a multi-line comment 
"""
# This is a single line comment


""" Variables and simple data types 
"""
fuenf = 5
pi = 3.1415926

Hello = "Hello"     # Strings can be written with inverted commas ...
World = 'World'       # ... OR simply with single comma.
                    # For better readability a style should be used consistently.
true = True 
false = False

# Date values are complex types
from datetime import date   # Import of a module with additional functions and/or classes
today = date(2020, 10, 6)
print(today)

# Current date/time: datetime.datetime.now()

# Attention: DYNAMIC TYPING
five = 5 
print(five)

five = "five" 
print(five)

# play with strings
language = "Python" 
version = 3
print("Programming with " + language + " " + str(version))
print("Programming with %s %s" % (language, version))         # % Operator;  at times hard to read
print("Programming with {0} {1}".format(language, version))   # str.format() with may options
print(f"Programming with {language} {version}")               # f-Strings; from Python 3.6

# Strong Typing -> EXPLICIT TYPE CONVERSION
a = "5" 
b = "6"
print(a + b)            # String-concatenate
print(int(a) + int(b))  # Addition of numbers


# Naming convention
"""
In Python you usually use
- sneak_case (I_consist_of_several_words)
- PascalCase (IConsist ofMultipleWords) 

camelCase, as known from other programming languages, is not used.

See https://www.python.org/dev/peps/pep-0008/ / 
"""


# ------------------------------------------------------------------------------

""" Moving on: Error tracking
"""
print("hello world") 
print("hello" + 13)

""" 
Ausgabe:

Traceback (most recent call last):
  File "main.py", line 1, in <module>
    print("Hello" + 13)
TypeError: can only concatenate str (not "int") to str

In most cases the error is recognized, identified and a solution is offered.
"""


# ------------------------------------------------------------------------------

""" 
Lists (like Arrays) 

- Elements are usually of the same type
"""
liste = list() 
print(liste)

students= ["Alice", "Bob", "Charlie", "David"] 
grades = [1, 2, 3, 4]
print(students)

# possible but not recommended
typmix = ["Value", 123, True] 
print(typmix)

# Find the length of the list
print(len(students))

# Elementes selection
"""
- Index starts with 0
- Inverse Index starts with -1
"""
print(students[0]) 
print(students[-1])

print(f"Student {students[2]} achieved {grades[2]} .")

print("python"[3])

# Lists in detail
"""
- Stack-Principle
"""
students.append("Eve") 
print(students)

# Lists concatenate

persons = ["Max", "Moritz"] + ["Lisa", "Lena"] 
print(persons)

# Remove elements from list 
"""
- Listenname.pop()
- Stack-Principle
"""

last = students.pop()
print(last) 
print(students)

# ... remove using index
del students[1] 
print(students)

# ... remove using value
students.remove("Charlie") 
print(students)

# attach a list to a string
print(", ".join(students))

# String spliting 
color = "Rot, Gelb, Grün, Blau" 
print(color.split())

# Specification of the separator possible
print(color.split("l"))


# number of elements in a string 
# Combination of functions
sentence= "I am a sentence." 
print(len(sentence.split()))

# List-Slicing
students = ["Alice", "Bob", "Charlie", "David"] 
print(students[2:4])
print(students[1:-1])
print(students[0:-1])
print(students[:-1])

# works also with strings
print("Hello World!"[0:5])

# Nested Lists
#  MultiDimensional Lists

cities = [
    ["Berlin", "Wildau", "Potsdam"], 
    ["London", "Glasgow", "Liverpool"]
]
print(cities[0]) 
print(cities[0][1])

# ------------------------------------------------------------------------------

""" Controll Structures
"""

# comparison operators 
print(6 < 5) 
print(5 < 6)
word = "Hello"
print(word == "Hello")  # Vergleich mit ==, da einfaches = der Zuweisungsoperator ist
print(word == "World")
print(word != "World")

#￼Case Queries (if)
Currency = "€" 
if Currency == "€":      # Colon corresponds to the {} from other programming languages.
    print("Euro")        # Indentation of associated lines is a special feature of Python and is supposed to
                         # Especially improve the readability of code. Indentations are mandatory!
elif Currency == "$": 
    print("US-Dollar")
elif Currency == "¥": 
    print("Japanischer Yen")
else: 
    print("others")

# Boolean values and operators
# Logical AND
print(True and True) 
print(True and False) 
print(False and True) 
print(False and False)
# Logical OR
print(True or True) 
print(True or False) 
print(False or True) 
print(False or False)

if True:
    print("if is executed")

semester = 4
if not semester >= 5: 
    print("executed")
if semester < 5: 
    print("executed")

# Search in Liste
names = ["Alice", "Bob"]
if "Charlie" not in names:
    print("Charlie ist nicht in der Liste enthalten")
if not "Charlie" in names:
    print("Charlie ist nicht in der Liste enthalten")

# Loops (while)

# counter bases Loops
i = 0
while i < 5: 
    print(i)
    i += 1 

print("Hello World")

# endcounter based Loops
i = 0
while i in range(0, 5): 
    print(i)
    i += 1
    if i == 3:
        break   # breaks the loops execution

print("Hello World")

# Loops over list
i = 0
while i < len(students): 
    print(students[i])
    i += 1

# Loops (for)
lists = [2, 5, 8]
for i in lists:
    print(i)

lists = ["Alice", "Bob", "Charlie"]
for i in lists:
    print(i)

# E.g. add using for loops and range function
sum = 0
for i in range(1, 11): 
    sum += i

print(sum)

# Get the element on the index
range(0,5)[2]

for i in range(0, 5): 
    if i == 3:
        continue    # Directs the thread to continue
    print(i)
￼￼

# ------------------------------------------------------------------------------

""" 
Dictionaries (wie Hash tables)

- Key value pairs
    
"""
dictionary = dict() 
print(dictionary)

kfz_kennz = {"Berlin": "B", "Potsdam": "P", "Cottbus": "CB", "Berlin": " BER"}
print(kfz_kennz)

# Add Values
kfz_kennz["Frankfurt (OR)"] = "FF" 
print(kfz_kennz)

# Delete Elements from dictionary
del kfz_kennz["Cottbus"] 
print(kfz_kennz)

# get the elements
# Error, if element not found ...
print(kfz_kennz["Cottbus"])
# better:
print(kfz_kennz.get("Cottbus"))

# Is a single Element in Dictionary?
if "Berlin" in kfz_kennz: 
    print("Berlin ist enthalten")
if "Cottbus" in kfz_kennz: 
    print("Cottbus ist enthalten")
else:
    print("Cottbus ist nicht enthalten")

# Dictionaries AND Loopsn
for key in kfz_kennz: 
    value = kfz_kennz[key] 
    print(key) 
    print(value)

for key, value in kfz_kennz.items(): 
    print(key + ": " + value)


# ------------------------------------------------------------------------------

"""
Tupel

- immutable type
- BUT: tuple element can be of variable type (e.g. list, dictionary)
"""
t = (1,2,3) 
print(t)

# add the values
t.append(4)

# change the values is not possible
t[0] = 123

# Tupel as list elements
students = [ 
    ("Max Müller", 22), 
    ("Lisa Ludwig", 23)
]
for student in students: 
    print(student)
    
# direct get the values
for name, alter in students: 
    print(f"{name}, {alter}")


# ------------------------------------------------------------------------------

""" Funktions

- defined using the keyword def xyz():
- Inside the block code is written indented
"""

def print_me1(): 
    print("Programmieren ...") 
    print("... mit Python.")

print_me1()

def print_me2(name):    # Funktion with parameters
    print("Hier ist " + name)

print_me2("Alice") 
print_me2("Bob")

def print_me3(name, zaehler): 
    for i in range(0, zaehler):
        print(name) 
    
print_me3("Telematics", 3)
￼
def print_me3b(name, zaehler=1):    # For parameters standart arguments are given
                                    # Dadurch wird der Parameter optional.
    for i in range(0, zaehler):
        print(name) 

print_me3b("Telematics")

# Funktion with Return
def maximum(a, b): 
    if a < b:
        return b 
    else:
        return a 

result = maximum(4, 5)
print(result)

# Tupel for multiple return values
def StudentInfo():
    return ("Max Müller", 22, "Telematik")

name, alter, studiengang = StudentInfo()
print(name) 
print(alter) 
print(studiengang)

# Overview of Python-Funktions: https://docs.python.org/3/library/functions.html


# ------------------------------------------------------------------------------

""" User input
"""
name = input("Ihr Name? ")
print(name)

alter = int(input("Ihr Alter? "))
print(eingabe)

liste = list(input("Liste? "))  # Eingabe: ["wert1", "wert2", ...]
print(liste)

# besser:
liste = eval(input("Liste? "))
print(liste)

# eval() returns the datatype

name_AND_note = eval(input("Name AND Note: "))   # Eingabe: {"key1": value1, "key2": value2, ...}
print(name_AND_note)


# ------------------------------------------------------------------------------

""" Working with files
"""

# Simple Text data_file reading
# data_file to read ("r") opens
data_file = open("demo.txt", "r")
# data_file line wise processing
for row in data_file:
    print(row.strip())     # strip() removes empty spaces

data_file = open("demo.txt", "r")
for row in data_file:
    print(row[-1] == "\n") # if the last character reached, step down one row
￼
# Write to a textdata_file
# open data_file for writing ("w": write)
# w overwrites data_file content; a (append) appends content
data_file = open("neu.txt", "w")
students = ["Alice", "Bob", "Charlie"]
for student in students:
    # Each element will be written on one separate line 
    data_file.write(student + "\n")
# File will be closed
data_file.close()

# with-Construct with implicit open/close
with open("neu.txt", "r") as data_file: 
    for zeile in data_file:
        print(zeile)

# CSV-Files Read
with open("data_file.csv") as data_file: 
    for zeile in data_file:
        print(zeile.strip().split(";"))     # Semicolon is a division indicator
with open("data_file.csv") as data_file: 
    for zeile in data_file:
        daten = zeile.strip().split(";") 
        print(f"{daten[0]}: {daten[1]}")

""" TODO FOOD FOR THOUGHT:
How to escape the line with column names?
"""


# ------------------------------------------------------------------------------
""" Classes AND Objects
"""

# In Python EVERYTHING is an object
# Numbers are objects
a = 5 
print(type(a))

# Operations are executed internally via corresponding functions 
# Example: Addition in object oriented notation
a = 3.5
a.__add__(5)

# Strings are objects
s = "Hello World" 
print(type(s))

len(s)
# ... internally executed as ...
s.__len__()

# Corresponding functions can be defined by the user
class A:
    def __len__(self):
        return 6 

instanz = A()
len(instanz)

# Define your own class
class Student():
# self is placeholder for each instance
    def name(self):
        print(f"{self.first_name} {self.last_name}")

class Company():
    def name(self):
        print(f"{self.company_name}: {self.company_type}")

#￼Instance of student class
sarah = Student()
sarah.first_name = "Sarah" 
sarah.last_name = "Schulze" 
sarah.Street = "Street 18"
print(sarah.first_name) 
print(sarah.last_name) 
print(sarah.Street)

tobias = Student()
tobias.first_name = "Tobias" 
tobias.last_name = "Thaler"
print(tobias.first_name) 
print(tobias.last_name)

f = Company()
f.company_name = "Max Müller" 
f.company_type = "GmbH"
f.name()

# call the methods
sarah.name()

# Define constructor
"""
method __init__ is the constructor 
__attribute or __method = private attribute or method
"Private" means: Avoid that subclasses overwrite attributes OR methods
"""
class Student():
    def __init__(self, first_name, last_name): 
        self.first_name = first_name 
        self.last_name = last_name 
        self.semester = 1
        
    def info(self):
        return f"{self.first_name} {self.last_name} (Semester: {self.semester})"

    def change_semester(self):
        self.semester = self.semester + 1

erik = Student("Erik", "Eisberg") 
print(erik.info())

erik.change_semester() 
print(erik.info())

# Inheritance

# Parent class is given as a parameter
class Intern(Student):
    def __init__(self, first_name, last_name, Company): 
        # init()-Methode of the parent class
        super().__init__(first_name, last_name) 
        self.Company = Company

    def info(self):
        return super().name() + " (" + self.Company + ")"

student = Intern("Jens", "Jensen", "Juni GmbH") 
print(student.name())

students = [
    Intern("Maxi", "Mayer", "Meister GmbH"), 
    Student("Jonas", "Just"),
    Student("Florian", "Finster"), 
    Intern("Carola", "Chor", "China AG")
]

for student in students: 
    print(student.name())


# ------------------------------------------------------------------------------

""" Exceptions and Error Handling
"""

def calculate(a, b): 
    print(a / b)

try: 
    calculate(5, 0)
except ZeroDivisionError:
    print("Division by zero is prohibited!")


try:
    filename="file.xyz"
    with open(filename, "r") as file: 
        print(file)
    print(5 / 0)
except ZeroDivisionError:
    print("Division by zero is prohibited!") 
except FileNotFoundError:
    print(f"No file is found of the name {filename}")

# Eigene Fehlerbehandlung implementieren
class UngueltigeEmail(Exception): 
    pass

def sende_email(email, betreff, inhalt): 
    if not "@" in email:
        raise UngueltigeEmail("E-Mail-Adresse enthält kein @-Zeichen")

try:
    sende_email("Hello", "Betreff", "Inhalt") 
    print("E-Mail erfolgreich gesendet.")
except UngueltigeEmail:
    print("Bitte eine gültige E-Mail-Adresse angeben.")

try:
    sende_email("Hello@example.com", "Betreff", "Inhalt") 
    print("E-Mail erfolgreich gesendet.")
except UngueltigeEmail:
    print("Bitte eine gültige E-Mail-Adresse angeben.")

#￼Aufräumen (finally)
try:
    data_file = open("data_file.xyz", "r")
    print(data_file)
except FileNotFoANDError:
    print("data_file wurde nicht gefANDen") 
finally:
    data_file.close() 
    print("¯\_(ツ)_/¯")


# ------------------------------------------------------------------------------

""" Module
"""
# Example to examine date and times (see https://docs.python.org/3/library/datetime.html 
import datetime as dt 
now = dt.datetime.now()
print(now)

# from .. import .. no need to enter the modul name
from datetime import date, time 
d = date(2019, 9, 26)
print(d)
t = time(15, 0, 0) 
print(t)

# ------------------------------------------------------------------------------

"""
Last Changes: 2020-10-06
"""
