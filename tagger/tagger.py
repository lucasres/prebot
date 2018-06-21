from urllib.parse import to_bytes
from nltk.corpus import floresta
from utilities.normalizeText import normalizeText
from utilities.support import prebotSupport
from stem.stem import stemming

class tagger():

	def __init__(self):
		"""
		construct of the class, this import all tagger of floresta 
		corpota
		"""
		self._taggers = floresta.tagged_words()
		self._nt = normalizeText()
		self._sp = prebotSupport()
		self._stem = stemming()

	def searchTagger(self,word):
		"""
		Search in corpora for word and return word and tagger in list
		:param word: String
		:return: List
		"""
		word = self._nt.lowerCase(word)
		for tag in self._taggers:
			if(self._stem.stemmingWord(word) == self._stem.stemmingWord(tag[0])):
				return tag
		return (word,None)



	def taggerPhrase(self,phrase):
		"""
		Split phrase in tokens and tagger all words
		:param phrase: String
		:return: List
		"""
		aux = []
		phrase = self._nt.lowerCase(phrase)
		tokens = self._sp.string2Token(phrase)
		for tk in tokens:
			rs = self.searchTagger(tk)
			if(rs[1] != None):
				aux.append((rs[0],rs[1].split("+")[1]))
			else :
				aux.append((rs[0],None))
		return aux