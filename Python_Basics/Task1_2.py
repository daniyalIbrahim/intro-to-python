#!/usr/bin/env python3
# Author    Daniyal Ibrahim | Telematics Engineer
# Date      20.10.2020
# Python    3.7.5

def readFile(name):
	names=[]
	f=open(name,"r")
	if f.mode=='r':
		lines=f.readlines()
		for line in lines:
			temp=line.partition("@")
			newtemp=temp[0].partition(".")
			names.append(newtemp[0]+" "+newtemp[2])
		return names


def writeFile(names):
	f = open("names.txt", "w+")
	for name in names:
		f.write(name+"\n")


if __name__=="__main__":
	filepath=input("please enter file path: ")
	names=readFile(filepath)
	writeFile(names)
