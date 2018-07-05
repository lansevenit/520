#!/usr/bin/python3

# acrescentando indice em cada linha exemplo: 1- daniel

with open('fruta.txt', 'r')as arquivo:
    var = arquivo.readlines()
    alterado = []

    cont = 1
    for linha in var:
        linha = linha.replace( '\n', '-{}\n'.format(cont))
        alterado.append(linha)
        cont +=1
        