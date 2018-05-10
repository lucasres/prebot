# -*- coding: latin-1 -*-
from normalizeText import normalizeText
from spellChecker import spellChecker
from stopWords import stopWord
from support import prebotSupport
from conf import conf
import os

class facadePrebot():
    def __init__(self,lang,cogroo= False):
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
        #if cogroo is necessary
        if(cogroo):
            pass

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

    def wrongSpace(self,pInput):
        """
        Call wrongspace in NormalizeText class
        :param inp: String
        :return: String
        """
        return self._normalizeText.wrongSpaces(pInput)

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

    def upperCase(self,pInput):
        """
        Call upperCase in NormalizeText class
        :param pInput: String
        :return: String
        """
        return self._normalizeText.upperCase(pInput)

    def lowerCase(self,pInput):
        """
        Call lowerCase in NormalizeText class
        :param pInput: String
        :return: String
        """
        return self._normalizeText.lowerCase(pInput)

    def removeSpecialCharacter(self,pInput):
        """
        Call removeSpecialCharacter in NormalizeText class
        :param pInput: String
        :return: String
        """
        return self._normalizeText.removeSpecialCharacter(pInput)

    def firstUpper(self,phrase):
        """
        Call fristUpper in normalizeText class
        :param phrase: String
        :return : String
        """
        return self._normalizeText.firstUpper(phrase)

    def spellChecker(self,pInput,wordsPath=None,tk = False):
        """
        Call spellchecker in NormalizeText class
        :param pInput: String
        :param wordsPath: Optional String
        :return: String
        """
        if(wordsPath is None):
            sp = spellChecker(self._lang, os.path.join("lang",self._lang,"wordsCorrect.txt"))
            return sp.fixThePharse(pInput)
        else:
            sp = spellChecker(wordsPath)
            return sp.fixThePharse(pInput)

    def countWord(self,phrase):
        """
        Call countWord in support Class
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
            rs = stopWord(self._lang ,os.path.join("lang",self._lang,"stopWords.txt"))
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