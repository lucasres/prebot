import os
import sys
sys.path.append(os.path.abspath(__file__)[:-10])
from utilities.support import prebotSupport
from tagger.tagger import tagger
from utilities.normalizeText import normalizeText
from spellChecker import spellChecker
from stopWords import stopWord
from stem.stem import stemming

class prebotFacade():
    def __init__(self,classes=['normalizeText','tagger','stem','stopWord','spellCheck']):
        """
        The constructor calls all subsystems.
        """
        self._support = prebotSupport()
        self._classes = classes
        if("tagger" in self._classes):
            self._tagger = tagger()
        if("normalizeText" in self._classes):
            self._normalize = normalizeText()
        if("spellCheck" in self._classes):
            self._spellChecker = spellChecker()
        if("stopWord" in self._classes):
            self._stopWord = stopWord()
        if("stem" in self._classes):
            self._stem = stemming()

    def token2String(self,tokens):
        """
        This method convert on list of tokens in string data.
        :param tokens: List
        :return: String
        """
        return self._support.token2String(tokens)

    def string2Token(self,phrase):
        """
        Convert a phrase in token list
        :param phrase: String
        :return: List
        """
        return self._support.string2Token(phrase)

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

    def bagOfWords(self,phrase):
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

    def taggerPhrase(self,phrase):
        """
        Tagger all word of the phrase using the corpora floresta
        :param phrase: String
        :return: List
        """
        return self._tagger.taggerPhrase(phrase)

    def removePunctuation(self,phrase):
        """
        Remove pontuaction of the phrase
        :param phrase: String
        :return: String
        """
        return self._normalize.removePunctuation(phrase)

    def removeWrongSpaces(self,phrase):
        """
        Remove all wrong space
        :param phrase: String
        :return: String
        """
        return self._normalize.wrongSpaces(phrase)

    def splitInPhrase(self,text):
        """
        Split text in list of phrase
        :param text: String
        :return: List
        """
        return self._support.splitInPhrase(text)

    def removeSpecialCharacter(self,phrase):
        """
        This method remove special character like ç.
        :param phrase: String
        :return: String
        """
        return self._normalize.removeSpecialCharacter(phrase)

    def fixThePharse(self,phrase):
        """
        this method corrects the orthography of the sentence based on the correction file, all words correct are found in correctWords
        :param phrase: String
        :return: String
        """
        return self._spellChecker.fixThePharse(phrase)

    def removeStopWords(self,phrase):
        """
        Remove all stop words, the stops words are found in file stopWords
        :param phrase:
        :return:
        """
        return self._stopWord.removeStopWord(phrase)

    def wrongSpaces(self,phrase):
        """
        Correct the wrong space
        :param phrase: String
        :return: String
        """
        return self._normalize.wrongSpaces(phrase)

    def firstUpper(self,phrase):
        """
        Upper case in first character
        :param phrase: String
        :return: String
        """
        return self._normalize.firstUpper(phrase)

    def lowerCase(self,phrase):
        """
        Get phrase with all words in lower case
        :param phrase: String
        :return: String
        """
        return self._normalize.lowerCase(phrase)

    def stemWord(self,word):
        """
        This method stem one word
        :param Word: String
        :return: String
        """
        return self._stem.stemmingWord(word)