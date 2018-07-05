#!/usr/bin/python3


# criar um dicionario de frutas e armazenar nome e valor

frutas = [
{'fruta':'uva','preco':2.0},'qtd': 10}, 
{'fruta':'abacaxi','preco':5.55,'qtd':20},
{'fruta':'banana', 'preco':4.5,'qtd' : 2}
{'fruta':'abacate', 'preco':7.0,'qtd': 4} 
{'fruta':'manga', 'preco':5.0,'qtd': 11}
]

# for fruta in frutas:
# print(fruta)


frutas2 = []
for fruta in frutas:
    fruta['preco'] += fruta['preco'] * 0.1
    frutas2.append(fruta)
print(frutas2)


soma = 0
for fruta in frutas:
    soma += fruta['preco'] * fruta['qtd']
    print('Total: {:.2f}'.format(soma))
    exit()
    frutas2 =[]

    


