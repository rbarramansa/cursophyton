#Faça um programa que leia o comprimento do cateto oposto e do
# cateto adjacente de um triângulo
# #retângulo e calcule e mostre o comprimento da hipotenusa.

from math import hypot
catoposto = float(input('Digite o tamanho do cateto oposto'))
catadjacente = float(input('Digite o tamanho do cateto adjacente'))
hipotenusa = hypot(catoposto,catadjacente)
print('O valor da hipotenusa é ?: {}'.format(hipotenusa))
