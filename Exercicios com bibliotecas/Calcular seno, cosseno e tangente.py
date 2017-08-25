#Criar um programa que leia um ângulo, e informe o valor do seno, cosseno e tangente.

from math import sin,cos,tan
angulo = float(input('Informe o valor do ângulo\n'))
seno = sin(angulo)
cosseno = cos(angulo)
tangente = tan(angulo)
print('O valor do ângulo é:{}\nO valor do seno é:{}\nOvalor do cosseno é:{}\nO valor da tangente é:{}\n'.format(angulo,seno,cosseno,tangente))