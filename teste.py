# -*- coding: latin-1 -*-
from facadePrebot import facadePrebot

teste = facadePrebot("pt-br")

#wrong space broker
print(teste.removeSpecialCharacter("oláa, oi"))

print(teste.spellChecker("oq vc gosta de fazer"))

print(teste.removeStopWords("ola eu sou o lucas e voce"))

print(teste.token2String(['teste','de','token']))

print(teste.string2Token("teste de token"))

print(teste.wrongSpaces("teste                de correçao de espaços"))

print(teste.firstUpper("ola quero upper no primeiro"))

print(teste.splitInPhrase("teste de split. segunda frase"))
