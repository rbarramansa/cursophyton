#Criar um programa que leia o nome completo e:
#Apresente letra em maiusculo
#Apresente letra em minusculo
#Qnts letras sem considerar os espaços
#Qnts letras tem o primeiro nome

nome = str(input('Digite seu nome completo'))
nomedividido = nome.split()
print(nome.upper())
print(nome.lower())
print(len(''.join(nomedividido)))
print(len(nomedividido[0]))
