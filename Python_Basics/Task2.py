#!/usr/bin/env python3
# Author    Daniyal Ibrahim | Telematics Engineer
# Date      20.10.2020
# Python    3.7.5

articles ={
    "apfel": 30,
    "birne": 20,
    "banane": 30,
    "traube": 10,
    "avocado": 50,
}

def getPriceTable(article:str= None, numOfArticles:int= 0, increment:int=1,discount:float=0):

	if not article:
		raise Exception("No article selected")
	#the article name converted to lowercase style
	articleLower=article.lower()
	try:
		articlePrice=articles[articleLower]
	except KeyError:
		raise Exception("article is not defined")
	if int(increment)>=5 and float(discount)!=0:
		dis = float(discount)
		totalprice= articlePrice * dis * int(numOfArticles)
		return str(numOfArticles)+" Stück "+article.upper()+" kostet "+str(totalprice)+" EUR"
	else:
		totalprice= articlePrice * int(numOfArticles)
		return str(numOfArticles)+" Stück "+article.upper()+" kostet "+str(totalprice)+" EUR"

if __name__=="__main__":
	result=[]
	try:
		temp=getPriceTable("Birne","3","2","0.6")
		result.append(temp)
		print(result)
		another=getPriceTable("avocaDo","15","7","0.6")
		result.append(another)
		print(result)
	except Exception as e:
		print(e)

