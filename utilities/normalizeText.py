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
        aux = sub(" +"," ",pInput)
        pun = ['.',',','!','?']
        #check if is space in 0 index of string
        if(aux[0] is " "):
            aux = aux[1:]
        #check is pontuaction
        for i in range(len(aux)):
            if((aux[i] in pun) and (aux[i-1] is " ")):
                aux = aux[:i-1] + aux[i:] 
        return aux

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
        aux = ''
        return aux.join(tmp for tmp in pharse if tmp not in punctuation)

    def firstUpper(self,phrase):
        """
        Make frist letter uppercase
        :param phrase: String
        :return : String
        """
        return phrase.capitalize()