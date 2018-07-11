#!/usr/bin/python3

with open('frutas.txt','a') as arquivo:
    arquivo.write('laranja\n')
print(arquivo.readline())

with open('frutas.txt', 'r') as arquivo:
    print(arquivo.readline())
arquivo.seek(0) 
    

# -----------------------------

'''
criar uma cópia do arquivo.txt acrescentando indice em cada linha

exemplo: 1- daniel

'''

with open('frutas.txt', 'r') as arquivo:
    var = arquivo.readlines()
alterado = []
cont = 1
for linha in var:
    alterado.append('{}-{}'.format(cont, linha))
cont += 1
print(alterado)

exit()

# abrindo um arquivo com 'a' para poder escrever.

with open('novo.txt', 'a') as arquivo:
    for linha in alterado:
        arquivo.wite(linha)

