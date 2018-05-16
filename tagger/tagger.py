import nltk
from nltk.corpus import floresta

class tagger():

	def __init__(self):
		"""
		construct of the class, this import all tagger of floresta 
		corpota
		"""
		self._taggers = floresta.tagged_words()

	def searchTagger(self,word):
		"""
		Search in corpora for word and return word and tagger in list
		:param word: String
		:return: List
		"""
		for tag in self._taggers:
			if(word == tag[0]):
				return tag

t = tagger()
print(t.searchTagger("informação"))

