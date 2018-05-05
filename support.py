from normalizeText import normalizeText


class prebotSupport:
    def __init__(self):
        """
        Construct of the class
        """
        pass

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