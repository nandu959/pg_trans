import pandas as pd

class App:
	dictionary = {}
	acmDAO=None
	method_names=[]
	dictionaries={}
	
	def __init__(self):
		acmDAO = AcmDAO()

	def loadJournal(self):
		obj = acmDAO.getJournal()
		method_names = dir(obj)
		objectsList = []
		for x in method_names:
			objectsList.append(getattr(obj, x))   #Adds all method objects in list
		
		for k in objectsList:
			print k  	#calling method objects -returns the value for each object in the objects list
						#Put it in a dictionary as key value pair

	def addToDict(self):
		obj = acmDAO.getJournal()
		method_names = dir(obj)
		
		for x in method_names:
			dictionary[x] = getattr(obj, x)   #Adds all method objects in to a distionary in key value pairs

	def loadJournals(self): 
		# To load a list of FJournal objects,convert it from dll to python data and store it into a dictonary
		journals = acmDAO.getJournals()
		var i =0
		for journal in journals:
			method_names = dir(journal)

			for x in method_names:
				dictionary[x] = getattr(journal, x)

			dictionaries[i] = dictionary
			i += 1

	def populateDataFrame(self):
		self.loadJournals()
		# To do transformations and actions on a dataframe 
		# reference http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html
		pdf = pd.DataFrame(dictionaries)
		print pdf





