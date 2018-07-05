#!/usr/bin/python3

# script para abertura de arquivos


with open ('nome','r') as arquivo:
conteudo = arquivo.readlines()
return conteudo


# automatizando criando uma função

def ler_arquivo(nome):
    with open(nome, 'r')
    conteudo = arquivo.readlines
    return conteudo

# chamada para 7uma variavel
variavel1 = ler_arquivo('frutas.txt')
variavel2 = ler_arquivo('nomes.txt')
variavel = ler_arquivo('times.txt')

print(variavel1)
print(variavel2)
print(variavel3)

exit()

# loop

while true:
    arq =input('digite o nome do arquivo ou sair: ')
    if arq == 'sair':
        break
        print(ler_arquivo(arq))



def ler_arquivo(nome, modo= 'r', conteudo =None):
    if modo == 'r'
    with open(nome, modo) as arquivo:
        return arquivo.readlines()
        
    elif modo == 'a':
        with open(nome, modo) as arquivo:
            arquivo.write(conteudo)
            return True



manipular_arquivo('nomes.txt', 'r')
print(a)
