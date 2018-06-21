import nltk.corpus
from utilities.normalizeText import normalizeText
from utilities.support import prebotSupport
from stem.stem import stemming


class TaggerMac():
    def __init__(self):
        """
        Construct of the class
        """
        self._words = nltk.corpus.mac_morpho.tagged_words()
        self._nt = normalizeText()
        self._sp = prebotSupport()
        self._stem = stemming()

    def getWords(self):
        """
        Get words of corpora mac morpho
        :return: List
        """
        return self._words

    def searchTagger(self, word):
        """
        Search in corpora for word and return word and tagger in list
        :param word: String
        :return: List
        """
        word = self._nt.lowerCase(word)
        print(word)
        for tag in self._taggers:
            if (self._stem.stemmingWord(word) == self._stem.stemmingWord(tag[0])):
                return tag