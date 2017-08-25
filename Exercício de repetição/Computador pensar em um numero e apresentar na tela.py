#Escreve um programa que faça o computador pensar em um numero de 0 a 5 e peça para o usuário descobrir
#qual foi o número que o computador escolheu.
#O programa deverá dizer se o computador acertou ou não

import random

num = random.randint(0,5)
usuario = int(input('Digite um número de 0 a 5'))

if num == usuario:
    print('Parabéns vc acertou o número que o computador escolheu foi o {}'.format(num))

else:
    print('Infelizmente você errou o computador escolheu o numero {}, e vc o numero {}'.format(num,usuario))

