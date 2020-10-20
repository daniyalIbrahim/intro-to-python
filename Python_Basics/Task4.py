#!/usr/bin/env python3
# Author    Daniyal Ibrahim | Telematics Engineer
# Date      20.10.2020
# Python    3.7.5
from csv import DictReader
from time import time

def read_csv(file_path):
	counter=0
	dictionary_of_names={}
	start=time()
	with open(file_path) as names:
		for row in DictReader(names):
			if row['Name'] == 'Max' and 1950 <= int(row['Year']) <= 2000 and row['State'] == 'CA':
				counter += int(row['Count'])
		print(f"{counter} times the name Max was appeared in {time() - start} seconds")


if __name__=="__main__":
	read_csv("names.csv")
