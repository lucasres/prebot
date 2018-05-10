# -*- coding: latin-1 -*-
from facadePrebot import facadePrebot

teste = facadePrebot("pt-br")

#wrong space broker
print(teste.removeSpecialCharacter("ol�a, oi"))

print(teste.spellChecker("oq vc gosta de fazer"))

print(teste.removeStopWords("ola eu sou o lucas e voce"))

print(teste.token2String(['teste','de','token']))

print(teste.string2Token("teste de token"))

print(teste.wrongSpaces("teste                de corre�ao de espa�os"))

print(teste.firstUpper("ola quero upper no primeiro"))

print(teste.splitInPhrase("teste de split. segunda frase"))
