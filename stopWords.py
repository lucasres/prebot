import os
from utilities.support import prebotSupport
import sys

class stopWord():

    def __init__(self,lang="portuguese" ,path = ""):
        """
        Construct of the class
        :param lang: String
        :param path: String
        """
        if(not path):
            self._path = os.path.join(sys.path[-1],"lang",lang,"stopWords.txt")
        else:
            self._path = path
        self._lang = lang
        self.stopWords = self.getStopWordsFromFile()

    def setPath(self,path):
        """
        Change path of the stopWords list
        :param path: String
        :return:
        """
        self._path = path

    def getPath(self):
        """
        Return the current path of stopwords
        :return: String
        """
        return self._path

    def getStopWordsFromFile(self):
        """
        Get all stopwords of the file
        :return: List
        """
        aux = []

        with open(self._path, 'r', encoding='utf8') as f:
            content = f.readlines()
        # you may also want to remove whitespace characters like `\n` at the end of each line
        content = [x.strip() for x in content]
        for word in content:
            # get in 0 word wrong and 1 word correct
            aux.append(word)
        return aux

    def getStopWords(self):
        """
        Get list of stop words
        :return: List
        """
        return self.stopWords


    def removeStopWord(self,pharse):
        """
        Remove all stop word of phrase
        :return: List
        """
        ps = prebotSupport(self._lang)
        aux = ps.string2Token(pharse)
        for tk in aux:
            if(tk in self.stopWords):
                aux.remove(tk)

        return aux;
