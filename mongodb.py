#!/usr/bin/python3

from pymongo import MongoClient

try:
    client = MongoClient()
    db = client['4linux']
except Exception as e:
    print("ERRO:{}".format(e))

# dados = db.pessoas.find_one({'_id':2}) busca informações na tabela
#print(dados)

# db.pessoas.remove() remove a informação do banco

# db.pessoas.insert({'_id' :5, 'nome' : 'joazinho'}) adiciona informacao no banco

# db.pessoas.update({'_id':5}, {'sobrenome' : 'silva'}) atualiza informação do banco