Daniyal Ibrahim | Telematics Engineer | Python 3.7.5 

Internet Programming Python and Javascript
---

Basics of Programming in Python 
=================================================

The following tasks should help to deepen the understanding of the basics of working with Python.


Task 1
---------

Subtask 1:

Create a (Python) list with email addresses. From this list the names are to be output.  
For example: If the e-mail address is Max.Muster@th-wildau.de, the name "Max Muster" (without quotation marks) should be output.

Subtask 2:

Provide the e-mail addresses in a text file. Read out the file and write the extracted names into a new file.   


Task 2
---------

Create a function that creates a price table for given items. Articles and prices should be available as dictionary.  
As function arguments an article description, the max. number of pieces to be issued as well as (optional) a step size for prices to be determined and (also optional) a percentage quantity discount are passed.  
The output should display the prices for one piece up to the max. number of pieces as a (Python) list. If no step size is specified, the step size is 1. The quantity discount should only be applied if the step size is at least 5.

Each output should be formatted for each line following: X pieces of ARTICLE NAME cost Y EUR. For one piece, the output must be adjusted accordingly (see example).

Example:

Dictionary:  
        {"apple":3, "pear":5}

Function call:  
        get_price_table("pear", 3, 2)
or alternatively  
        get_price_table(product = "pear", number_of_pieces = 3, increment = 2)

output:  
        ["1 piece of pear costs 5 EUR", "2 pieces of pear cost 10 EUR", "3 pieces of pear cost 15 EUR"]

Also handle the case that an article description can be entered differently (upper/lower case) or incorrectly. An error message must be issued if the entry is incorrect.

Task 3
---------
A rudimentary ATM is to be implemented. The functions are described in the following subtasks.

Subtask 1:

Create an account class (Account) with the property account balance (credits). This property is initialized with a starting capital. The method display should show the current account balance. 

Subtask 2:

Add two methods for depositing (pay_in) and withdrawing (withdraw) to the class. The account balance should be adjusted accordingly for deposits and withdrawals.

It should only be possible to withdraw money as long as there is money in the account (no overdraft credit). In case of a possible overdraft, an error message should be displayed. This message should indicate the maximum amount of money that can be withdrawn.

Subtask 3:

A PIN should be used to protect the account access.
Add a property pin to the class. This property should also be initialized.

Note that now, when withdrawing money, the PIN must be specified in addition to the amount. If the PIN is incorrect, an error message should be displayed.



Task 4
---------

D
The file names.csv.zip contains a summary of the frequencies of given first names per US state in the years from 1910 to 2014.  
The data are available in CSV format (first row contains column descriptions). The uncompressed file is about 150 MB in size and contains over 5.5 million entries.

Subtask 1:

Determine how often the name "Max" was used as a male first name in California between 1950 and 2000.

Subtask 2:

Determine which name in total was most frequently used in the entire USA over all time periods.

Notes on processing:
* Read the data into a dictionary. Count how often each first name occurs in total.
* Then analyze the dictionary to find the most common first name.


---


Last Changes: 2020-10-06

