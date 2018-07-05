#!/usr/bin/python3
nome = input("Digite o nome do aluno:")
nota1 = int(input("Digite a primeira nota: \n"))
nota2 = int(input("Digite a segunda nota:  \n")) 
media  = (nota1 + nota2) / 2
print(" O aluno {} tem \ a media {}".format(nome, media))


nome  = input("Digite o nome do aluno")
nota1 = input("Digite a primeira nota")
nota2 = input("Digite a segunda nota")
media  = (nota1 + nota2) / 2 
if media >= 7:
        result = 'Aprovado'
elif media < 7 and media > 4:
        result = 'Recuperacao'
else
        result = 'Reprovado'

print("""O aluno {}
            Media: {}
            Resultado: {} """.format(nome,media, result))
