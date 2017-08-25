#Crie um programa para mostrar o primeiro nome e o último sobrenome

nome = str(input('Digite seu nome completo'))
nomedividido = nome.split()

print(nomedividido[0], nomedividido[-1])