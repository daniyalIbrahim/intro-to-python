#!/usr/bin/env python3
# Author    Daniyal Ibrahim | Telematics Engineer
# Date      20.10.2020
# Python    3.7.5
from datetime import datetime

class Account:

	def __init__(self, credits:int, pin:int):
		self.credits = credits
		self.pin = pin
		now = datetime.now()
		self.now=now

	def display_balance(self):
		format_string = self.now.strftime("%d.%m.%Y %H:%M:%S")
		print("___________________________________________")
		print("Current Time:\t\t", format_string)
		print("Current Balance:\t\t", self.credits)
		print("___________________________________________")

	def deposit(self, amount:float):
		now = datetime.now()
		time_str= now.strftime("%d.%m.%Y %H:%M:%S")
		new_amount = self.credits+amount
		self.credits = new_amount
		print("Your new credit:\t",self.credits)
		print("Time:\t\t", time_str)


	def withdraw(self,amount:float,pin:int):
		if pin==self.pin:
			if self.credits >= amount:
				now = datetime.now()
				time_str = now.strftime("%d.%m.%Y %H:%M:%S")
				print("sucessfully withdrawn the amount ",str(amount))
				new_amount = self.credits - amount
				self.credits = new_amount
				print("Time",time_str)
			else:
				now = datetime.now()
				time_str = now.strftime("%d.%m.%Y %H:%M:%S")
				print("Your credit is not enough for this transaction!")
				print("Time:	", time_str)
		else:
			now = datetime.now()
			time_str = now.strftime("%d.%m.%Y %H:%M:%S")
			print("You entered an incorrect pin!")
			print("Time:    ", time_str)



def Welcome():
	now = datetime.now()
	time_str = now.strftime("%d.%m.%Y %H:%M:%S")
	print("################################################")
	print("________________WELCOME TO ATM__________________")
	print("__CURRENT DATE & TIME:",time_str)
	print("\n")
	print("################################################")
	print("\n")


if __name__=="__main__":
	Welcome()
	account = Account(1000,8525)
	while True:
		try:
			entered_pin=input("Please enter your pin to continue:")
			pin = int(entered_pin)
		except ValueError:
			print("Valid Number please")
			continue
		if pin==account.pin:
			account.deposit(100)
			account.display_balance()
			account.withdraw(11,pin)
			account.display_balance()
		else:
			print("Dont play around")
			print("The last pin you entered was incorrect")

