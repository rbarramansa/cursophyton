#Ler duas notas e calcular a média

aluno = str (input('Digite o seu nome'))
nota1 = int (input('Digite a primeira nota'))
nota2 = int (input('Digite a segunda nota'))
media = (nota1 + nota2)/2
print(' O aluno {}, tirou {} na primeira prova, na segunda tirou {} a média dele ficou em {}'.format(aluno,nota1,nota2,media))