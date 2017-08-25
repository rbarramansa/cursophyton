#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados
#Ex : Digite um número : 1834
#Unidade
#dezena
#centena
#milhar

num = str(input('Digite um número'))
sespaco = num.strip()
print('Unidade',sespaco[0])
print('Dezena',sespaco[1])
print('Centena',sespaco[2])
print('Milhar',sespaco[3])