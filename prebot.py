import os
import sys
sys.path.append(os.path.abspath(__file__)[:-10])
from utilities.support import prebotSupport
from tagger.tagger import tagger

class prebotFacade():
    def __init__(self):
        """
        The constructor calls all subsystems.
        """
        self._support = prebotSupport()
        self._tagger = tagger()

    def token2String(self,tokens):
        """
        This method convert on list of tokens in string data.
        :param tokens: List
        :return: String
        """
        return self._support.token2String(tokens)

    def splitInSentence(self,text):
        """
        This method get a text and split in list of phrase
        :param text: String
        :return: List
        """
        return self._support.splitInPhrase(text)

    def countWord(self,phrase):
        """
        Count the number of words in a phrase
        :param phrase: String
        :return: Int
        """
        return self._support.countWord(phrase)

    def bagOfWord(self,phrase):
        """
        Vectoriza a phrase in the model bag of words
        :param phrase: String
        :return: List
        """
        return self._support.bagOfWords(phrase)

    def ngram(self,phrase,n,unity="word"):
        """
        Contains a n-item sequence of a statement. Since n is the number of items and unity the unit of the item (c = char or w = word)
        :param phrase: String
        :param n: Int
        :param unity: String
        :return: List
        """
        return self._support.ngram(phrase,n,unity)

    def taggerWord(self,word):
        """
        Tagger a word and return list of word and tagger
        :param word: String
        :return: List
        """
        return self._tagger.searchTagger(word)