#!/usr/bin/python3

from pymongo import MongoClient

try:
    client = MongoClient()
    db = client['4linux']
except Exception as e:
    print("ERRO:{}".format(e))

frutas = [    


 # {'_id':1', 'fruta':'laranja', 'preco':5, 'quantidade':10},
 #{'_id':2', 'fruta':'mamao',   'preco':5, 'quantidade':10},
 #{'_id':3', 'fruta':'maca',    'preco':5, 'quantidade':10},
 #{'_id':4', 'fruta':'abacate', 'preco':5, 'quantidade':10},

db.frutas.insert({'_id':1, 'abacate' : 'preco':5, 'quantidade':10}
