# Abrindo um arquivo, percorrer  Lista, escrever no arquivo, retornar treue ou false.

#!/usr/sbin/python3

# criando uma funcao para abrir um arquivo

def abrir_arquivo(nome_arquivo):
try
   with open(nome_arquivo, 'r') as) arq:
     arq.readlines(Conteudo)
     return True
except Excepetion as e:
    return 'Erro: {}'.format(e)

# criando uma funcao para esctrever em um arquivo


def escr_arq(nome_arq, contenudo):
    with open(nome_arq,'w')
        arq.writelines(conteudo)
        return True
       except Excepetion as e:
           return 'Erro: {}'.format(e)

nome = ['daniel\n','pedro\n','joao\n','julio\n']
escr_arq('nomes.txt', nomes'))

# criando e definindo uma funcao para alterar uma lista


def alterar_lista(lista):
    lista = []
    for x in lista:
        lista1.append('{}\n'.format(x))
    return lista1

# percorrendo um arquivo

nomes = ['fabio', 'fernando', 'jose', 'maria']
for x in nomes:
    nomes1.append('{}\n'.format())   

    print(nomes1)     


# chamar um funcao, lista

nomes = ['fabio', 'fernando', 'jose', 'maria']

print(alterar_lista(nomes))
exit()







exit()
