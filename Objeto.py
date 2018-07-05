#!/usr/bin/python3

class Dog():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.energia = 10

    def latir(self):
        print('Au au !')
    
    def andar(self):
        self.energia -= 1
        print('andando.... energia: {}'.format(self.energia))

    def dormir(self):
        self.energia = 10
        print('dormindo......')

dog1 = Dog('cezinha', 2)

dog1.latir()
dog1.andar()
print(dog1.idade)
print(dog1.energia)

    