#!/usr/bin/env python3
# Author    Daniyal Ibrahim | Telematics Engineer
# Date      20.10.2020
# Python    3.7.5
def getNamesFromEmail(email_list):
	names=[]
	for email in email_list:
		email_tuple=email.partition("@")
		name_tuple=email_tuple[0].partition(".")
		names.append(name_tuple[0]+" "+name_tuple[2])
	return names


def printNames(cleanNames):
	for name in cleanNames:
		print(name)
		print("\t")

def printHeader():
	print("----------------------------------------------------")
	print("-------------------WELCOME--------------------------")
	print("----Enter an Email address with the following-------")
	print("----pattern i.e. Max.Muster@abc.com-----------------")
	print("----& you will get the name returned without email--")

if __name__=="__main__":
	email_list=[]
	names_list=[]
	printHeader()
	print("\n ")
	while True:
		email=input("Please Enter an Email Address: \n")
		email_list.append(email)
		names_list=getNamesFromEmail(email_list)
		printNames(names_list)
		print("\n")
		print(str(len(email_list))+" elements are present in the Email List")
