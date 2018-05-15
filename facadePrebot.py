# -*- coding: latin-1 -*-
from normalizeText import normalizeText
from spellChecker import spellChecker
from stopWords import stopWord
from support import prebotSupport
from conf import conf
from stemming import stemming
from posTagger import posTagger
import os

class facadePrebot():
    def __init__(self,lang="portuguese"):
        """
        Construct of the class. When instantiated this method call the other class of the framework.
        :return:
        """
        #conf
        self._conf = conf()
        #setup language
        self._lang = self._conf.langExist(lang)
        #normalizing text class
        self._normalizeText = normalizeText()
        #support class
        self._suport = prebotSupport(lang)
        #stemming class
        self._stemming = stemming()
        #posttager class
        self._posTagger = posTagger()

    def getLang(self):
        """
        Retrun the language of framework
        :return: String
        """
        return self._lang

    def setLang(self,lang):
        """
        Set the new langague of framework
        :param lang: String
        :return:
        """
        self._lang = lang

    def wrongSpace(self,phrase):
        """
        Remove wrong spaces in the phrase
        :param inp: String
        :return: String
        """
        return self._normalizeText.wrongSpaces(phrase)

    def getSupport(self):
        """
        Return support class
        :return: Support Class
        """
        return self._suport

    def getNormalize(self):
        """
        Return normalizeText class
        :return: normalizeText Class
        """
        return self._normalizeText

    def conf(self):
        """
        Return conf class
        :return: conf Class
        """
        return self._conf

    def getLanguages(self):
        """
        Return all languages supported for framework
        :return: List
        """
        return self._conf.getLanguages()

    def upperCase(self,phrase):
        """
        Upper all words of the phrase
        :param phrase: String
        :return: String
        """
        return self._normalizeText.upperCase(phrase)

    def lowerCase(self,phrase):
        """
        Lower all words of the phrase
        :param phrase: String
        :return: String
        """
        return self._normalizeText.lowerCase(phrase)

    def removeSpecialCharacter(self,phrase):
        """
        Call removeSpecialCharacter in NormalizeText class
        :param phrase: String
        :return: String
        """
        return self._normalizeText.removeSpecialCharacter(phrase)

    def firstUpper(self,phrase):
        """
        Captalize the text
        :param phrase: String
        :return : String
        """
        return self._normalizeText.firstUpper(phrase)

    def spellChecker(self,phrase,wordsPath=None,tk = False):
        """
        Check if there is one in a sentence
        :param phrase: String
        :param wordsPath: Optional String
        :return: String
        """
        if(wordsPath is None):
            sp = spellChecker()
            return sp.fixThePharse(phrase)
        else:
            sp = spellChecker(wordsPath)
            return sp.fixThePharse(phrase)

    def countWord(self,phrase):
        """
        Count words of the phrase
        :param phrase: String
        :return : Int
        """
        return self._suport.countWord(phrase)

    def wrongSpaces(self,phrase):
        """
        Call wrongspace in normalize Class
        :param phrase: String
        :return: String
        """
        return self._normalizeText.wrongSpaces(phrase)


    def removeStopWords(self,phrase,stopWordsPath=None,tk=False):
        """
        Call remove stop words in stopWords Class
        :param phrase: String
        :return: String
        """
        if(stopWordsPath is None):
            rs = stopWord()
            if(tk):
                return rs.removeStopWord(phrase)
            else :
                return self._suport.token2String(rs.removeStopWord(phrase))
        else:
            rs = stopWord(stopWordsPath)
            if(tk):
                return rs.removeStopWord(phrase)
            else :
                return self._suport.token2String(rs.removeStopWord(phrase))

    def token2String(self,tokens):
        """
        Convert list of tokens in string
        :param tokens: List
        :return: String
        """
        return self._suport.token2String(tokens)

    def string2Token(self,phrase):
        """
        Convert strinf in tokens list
        :param tokens: String
        :return: List
        """
        return self._suport.string2Token(phrase)

    def splitInPhrase(self,text):
        """
        Split text phrase in list
        :param text: String
        :return : List
        """
        return self._suport.splitInPhrase(text)

    def stemmingPhrase(self,phrase):
        """
        Steamming all words of the phrase and return in list
        :param phrase: String
        :return: List
        """
        return self._stemming.stemmingPhrase(phrase)

    def stemmingWord(self,phrase):
        """
        Steamming all words of the phrase and return in list
        :param phrase: String
        :return: List
        """
        return self._stemming.stemmingWord(phrase)

    def posTaggerWord(self,word):
        """
        This method make postagger of the word
        :param word: String
        :return : List
        """
        return self._posTagger.posTaggergWord(word)

    def posTaggerPhrase(self,phrase):
        """
        This method make postagger in all word of the phrase and return in list
        :param phrase: String
        :return : List
        """
        return self._posTagger.posTaggerPhrase(phrase)
