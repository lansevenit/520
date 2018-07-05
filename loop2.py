#!/usrr//bin/python3
# ler nomes, adicionar em um arquivo.txt ate digitar sair, 
# mostrar a leitura no final.



# fazendo loop e abrindo o arquivo várias vezes

while True:
    nome = input('Digite um nome:')
    if nome.strip().lower() == 'sair':
        break
with open('nomes.txt', 'a') as arquivo:
    arquivo.write(nome + '\n')



# fazendo o loop abrindo o arquivo uma unica vez

# complementar[

with open('nomes.txt', 'a') as arquivo:
    nome = input('digite um none')
    if nome.strip().lower() == 'sair'





#####


