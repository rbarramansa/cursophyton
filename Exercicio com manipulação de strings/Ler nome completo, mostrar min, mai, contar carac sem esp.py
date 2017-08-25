#Criar um programa que leia o nome completo da pessoa e mostre:
#Letra maiuscula
#Letra minuscula
#Contar os caracteres não levando em consideração os espaços
#Contar os caracteres da primeira palavra

nome= str(input('Digite seu nome completo\n'))
nomedividido = nome.split()
print('O nome completo digitado é:\n{}\n'.format(nome))
print('O nome digitado com todas as letras em maiusculas é:\n{}\n'.format(nome.upper()))
print('O nome digitado com todas as letras em minusculas é:\n{}\n'.format(nome.lower()))
print('Este nome possui {} caracteres'.format(len(''.join(nomedividido))))
print('O primeiro nome digitado foi o {} e este possui {} caracteres'.format(nomedividido[0],(len(nomedividido[0]))))