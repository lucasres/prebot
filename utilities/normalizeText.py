# -*- coding: latin-1 -*-
from re import sub
from unicodedata  import normalize
from string import punctuation

class normalizeText():
    def __init__(self):
        """
            Construtor da classe
        """

    def wrongSpaces(self,pInput):
        """
        Corrige os espaços errados da entrada substituindo por um único espaço
        :param input: String
        :return: String
        """
        return sub(" +"," ",pInput)

    def upperCase(self,pInput):
        """
        Converte todos os caracteres da string em maiúsculo
        :param pInput: String
        :return: String
        """
        return pInput.upper()

    def lowerCase(self, pInput):
        """
        Converte todos os caracteres da string em minúsculo
        :param pInput: String
        :return: String
        """
        return pInput.lower()

    def removeSpecialCharacter(self,pInput):
        """
        Retira todo os acentos e caracteres epeciais da string
        :param pInput: String
        :return: String
        """
        return normalize('NFKD', pInput).encode('ASCII', 'ignore').decode('ASCII')

    def removePunctuation(self,pharse):
        """
        Remove all the punctuation of the pharse
        :param Pharse: String
        :return:String
        """
        return ''.join(c for c in pharse if c not in punctuation)

    def firstUpper(self,phrase):
        """
        Make frist letter uppercase
        :param phrase: String
        :return : String
        """
        return phrase.capitalize()