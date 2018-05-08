from normalizeText import normalizeText
import os

class prebotSupport:
    def __init__(self,lang):
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
        with open(os.path.join("lang",self.lang,"abbreviation.txt")) as f:
            content = f.readlines()
        content = [x.strip() for x in content]
        for ab in content:
            aux.append(ab)

        return aux

    def splitInPhrase(self,text,unit="string"):
        """
        Split text in phrase
        :param text: String
        :return: List     """
        aux = []
        rs = []
        text = text.lower()
        tokens = self.string2Token(text)
        if unit is "token":
            for tk in tokens:
                if tk[-1] is ".":
                    if tk in self.abbreviation:
                        aux.append(tk)
                    else:
                        aux.append(tk)
                        rs.append(aux)
                        aux = []
                else:
                    aux.append(tk)
        else:
            for tk in tokens:
                if tk[-1] is ".":
                    if tk in self.abbreviation:
                        aux.append(tk)
                    else:
                        aux.append(tk)
                        rs.append(self.token2String(aux))
                        aux = []
                else:
                    aux.append(tk)

        return rs

    def teste(self):
        print(self.abbreviation)
        if "dr." in self.abbreviation:
            print("ok")

teste = prebotSupport("pt-br")
print(teste.splitInPhrase("teste de frase do Dr. Lucas.resende final. sem atilizacao de abreviacao."))
