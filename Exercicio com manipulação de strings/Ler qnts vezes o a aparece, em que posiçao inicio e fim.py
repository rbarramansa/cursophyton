#Crie um programa que leia uma frase pelo teclado e responda :
#Quantas vezes a letra "a" aparece
#Em que posição ela aparece a primeira vez
#Em que posição ela aparece a última vez

frase = str(input('Digite uma frase'))
contagem = frase.count('a')
print('A frase possui {} letras A\nAparece a primeira vez na posição {} da lista\nAparece a última vez na posição {} da'
      ' lista'.format(contagem,frase.find('a'),frase.rfind('a')))
