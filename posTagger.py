import requests
from support import prebotSupport
class posTagger():
	def __init__(self,lang="portuguese"):
		"""
		Construct of the class
		:param lang: String
		:return:
		"""
		self._lang 		= lang
		self._headers 	= {'Content-type': 'application/json'}

	def posTaggergWord(self,word):
		"""
		This method make a call for end-point http://text-processing.com/api/stem/, for make posTagger of the word
		:param Word: String
		:return: String
		"""
		headers = self._headers
		body 	= {"text":word,"language":self._lang}
		r = requests.post("http://text-processing.com/api/tag/",headers=headers,data=body)
		return r.text[13:-3].split("/")

	def changeHeader(self,key,value):
		"""
		This method change header HTTP of post requisition
		:param key: String
		:param value: String
		:return:
		"""
		self._headers.update({key:value})

	def posTaggerPhrase(self,phrase):
		"""
		This method make posTagger in full phrase and return in list with word and pos tagging
		:param Phrase: String
		:return: List
		"""
		#control variables
		sp = prebotSupport(self._lang)
		aux = sp.string2Token(phrase)
		rs = []
		print(aux)
		#posTagger all words
		for tk in aux:
			rs.append(self.posTaggergWord(tk))

		return rs