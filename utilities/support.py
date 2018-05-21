from .normalizeText import  normalizeText
import os
import sys

class prebotSupport:
    def __init__(self,lang="portuguese"):
        """
        Construct of the class
        """
        self.lang = lang
        self.abbreviation = self.getAbbreviations()
        

    def string2Token(self,phrase):
        """
        Split phrase in tokens
        :param phrase: String
        :return: List
        """
        nt = normalizeText()
        phrase = nt.wrongSpaces(phrase)
        return phrase.split(" ")

    def token2String(self,tokens):
        """
        This method convert tokens in String
        :param tokens: List
        :return: String
        """
        aux = ""
        for token in tokens:
            aux = aux + " " + token

        return aux.strip()

    def countWord(self,phrase):
        """
        Count number of the word of one phrase
        :param phrase: String
        :return : Int  
        """
        aux = []
        aux = self.string2Token(phrase)
        return len(aux)

    def getAbbreviations(self):
        """
        Get list of abbreviations of the file
        :return: List
        """
        aux = []
        path = os.path.join(sys.path[-1],"lang",self.lang,"abbreviation.txt")
        with open(path) as f:
            content = f.readlines()
        content = [x.strip() for x in content]
        for ab in content:
            aux.append(ab)

        return aux

    def splitInPhrase(self,text,unit="string"):
        """
        Split text in phrase
        :param text: String
        :return: List
        """
        aux = []
        rs = []

        text = text.lower()
        tokens = self.string2Token(text)
        for tk in tokens:
            if (tk[-1] is ".") or (tk[-1] is ",") or (tk[-1] is "?") or (tk[-1] is "!"):
                if tk in self.abbreviation:
                    aux.append(tk)
                else:
                    aux.append(tk)
                    rs.append(self.token2String(aux))
                    aux = []
            else:
                aux.append(tk)

        return rs

    def bagOfWords(self, phrase):
        """
        Create the bag of words
        :param phrase: String
        :return: Dict
        """
        nt = normalizeText()
        aux = self.string2Token(nt.removePunctuation(phrase))
        bagWords = {}
        for tk in aux:
            if tk in bagWords:
                count = bagWords.get(tk)
                count += 1
                bagWords.update({tk: count})
            else:
                bagWords.update({tk: 1})

        return bagWords

    def ngram(self, phrase, n, unit="w"):
        """
        Return ngram of the phrase
        :param phrase: String
        :param n: Int
        :param unit: String
        :return: List
        """
        gram = []
        if (unit is "w"):
            aux = self.string2Token(phrase)
            if (len(aux) <= n):
                return aux
            else:
                loop = len(aux) - (n - 1)
                for i in range(loop):
                    gram.append(aux[i:i + n])
                return gram
        else:
            if (len(phrase) <= n):
                return phrase
            else:
                loop = len(phrase) - (n - 1)
                for i in range(loop):
                    gram.append(phrase[i:i + n])
                return gram