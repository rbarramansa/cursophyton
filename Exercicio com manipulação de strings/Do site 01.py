#
#Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento.
#Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo. o Compara duas strings o String 1: Brasil Hexa 2006 o String 2: Brasil! Hexa 2006! o Tamanho de "Brasil Hexa 2006": 16 caracteres o Tamanho de "Brasil! Hexa 2006!": 18 caracteres o As duas strings são de tamanhos diferentes. o As duas strings possuem conteúdo diferente.
#



frase1 = str(input('Digite a primeira frase :'))
frase2 = str(input('Digite a segunda frase'))
print('A frase 1 contém o seguinte texto:\n{}\nA frase 2 contém o seguinte texto:\n{}\n'.format(frase1,frase2))
print('A frase 1 contém o seguinte tamanho:\n{}\nA frase 2 contém o seguinte tamanho:\n{}\n'.format((len(frase1)),(len(frase2))))


