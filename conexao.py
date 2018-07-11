#!/usr/bin/python3
import psycopg2

try:
    con = psycopg2.connect('host=localhost dbname=projeto\
                user=admin password=4linux port=5432')
    print('canecto com sucesso')        
    cur = con.cursor()
    cur.execute("insert into pessoas(nome, idade, telefone)\
                    values('landre','44', 98989898)")
    con.commit()

    # conteudo = cur.fetchall()
    # print(conteudo)
except Exception as e:
    print('Erro conexao: {}'.format(e))

    #fetchall fetchone
