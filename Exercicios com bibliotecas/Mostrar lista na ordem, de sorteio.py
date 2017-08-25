import random
aluno1 = str(input('Digite o primeiro nome'))
aluno2 = str(input('Digite o segundo nome'))
aluno3 = str(input('Digite o terceiro nome'))
aluno4 = str(input('Digite o quarto nome'))
aluno5 = str(input('Digite o quinto nome'))
lista = [aluno1,aluno2,aluno3,aluno4,aluno5]
random.shuffle(lista)
print(lista)