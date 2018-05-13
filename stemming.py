import requests
from support import prebotSupport
class stemming():
	def __init__(self,lang="portuguese"):
		"""
		Construct of the class
		:param lang: String
		:return:
		"""
		self._lang 		= lang
		self._headers 	= {'Content-type': 'application/json'}

	def stemmingWord(self,word):
		"""
		This method make a call for end-point http://text-processing.com/api/stem/
		:param Word: String
		:return: String
		"""
		headers = self._headers
		body 	= {"text":word,"language":self._lang}
		r = requests.post("http://text-processing.com/api/stem/",headers=headers,data=body)
		return r.text[10:-2]

	def changeHeader(self,key,value):
		"""
		This method change header HTTP of post requisition
		:param key: String
		:param value: String
		:return:
		"""
		self._headers.update({key:value})

	def stemmingPhrase(self,phrase):
		"""
		This method make stemming in full phrase
		:param Phrase: String
		:return: List
		"""
		#control variables
		sp = prebotSupport(self._lang)
		aux = sp.string2Token(phrase)
		rs = []
		#stemming all words
		for tk in aux:
			rs.append(self.stemmingWord(tk))

		return rs