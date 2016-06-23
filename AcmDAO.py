from fatools import front
import acm

class AcmDAO :

	journalObj={}

	def __init__(self):
		front.connect()
		journalObj = acm.FJournal()


	def getJournal(self):
		# To load only one FJournal object
		journalObj = acm.FJournal()
		return journalObj

	def getJournals(self):
		# To load a list of FJournal objects
		list =[] # Need to find a way how to load a list of FJournals something like acm.FJournal().select()
		return list

	def updateJournal(self,id):
		# Need to implement based on a primary key
	def deleteJournal(self,id):
		# Just a sample method for future use Need to implement based on a primary key



