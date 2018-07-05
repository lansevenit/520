#!/usr/bin/python3

def boas_vindas(**Kargs):
    print(kargs)

boas_vindas(nome='daniel', sobrenome='prata')

def boas_vindas(**kargs):
    print("Ola {} {} seja bem vindo!" \ 
            ".format(kargs['nome'],kargs['sobrenome']))

 # dicionario =  #  dic = {'nome': 'daniel', 'sobrenome': 'prata'}


