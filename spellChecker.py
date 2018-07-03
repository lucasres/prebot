# -*- coding: latin-1 -*-
from utilities.support import prebotSupport
import os
import sys

class spellChecker():
    def __init__(self,lang="portuguese",path=""):
        """
        This is the construct of the class. Is responsable for load the words pattern that will usies in the spell checker
        :return:
        """
        if (not path):
            self._path = os.path.join(sys.path[-1], "lang", lang, "wordsCorrect.txt")
        else:
            self._path = path
        self.lang = lang
        self.WORDS = self.getWordsFromFile()

    def getwordsCorrect(self):
        """
        Return the current path of the spelling correct.
        :return: String
        """
        return self.wordsPath

    def setWordsPath(self,wordPath):
        """
        This method change the location of the path for correct word list
        :param wordPath: String
        :return:
        """
        self.wordsPath = wordPath


    def fixWord(self,target):
        """
        This method is responsable for fix the word
        :param target: String
        :return: String
        """
        for aux in self.WORDS:
            #check if is equal a word wrong
            if target == aux[0]:
                #if equals return the correct word
                return aux[1]
        #the word not in wrong list
        return target

    def fixThePharse(self,phrase):
        """
        This method does spelling correction
        :param Pharse: String
        :return: String
        """
        #result of correction
        rs = []
        sp = prebotSupport(self.lang)
        #get tokens
        tokens = sp.string2Token(phrase)
        for tkOnly in tokens:
            #correct all words of the list
            rs.append(self.fixWord(tkOnly))
        return sp.token2String(rs)

    def getWords(self):
        """
        Get words loads
        :return : List
        """
        print(self.WORDS)

    def getWordsFromFile(self):
        """
        Get all word od the file
        :return: List
        """
        aux = []

        with open(self._path, 'r', encoding='utf8') as f:
            content = f.readlines()
        # you may also want to remove whitespace characters like `\n` at the end of each line
        content = [x.strip() for x in content]
        for word in content:
            # get in 0 word wrong and 1 word correct
            aux.append(word.split(","))
        return aux