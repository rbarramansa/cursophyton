#Faça um programa que leia a altura e a largura de uma parede em metros, calcule sua área e
#e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma
#área de 2m²




altura = float(input('Digite a altura\n'))
largura = float(input('Digite a largura\n'))
area = altura * largura
tinta = area/2
print('A altura digitada foi:\n{}\nA largura digitada foi:\n{}\nÁ área a ser pintada foi de:\n{} metros\nSerá necessário {} litros '
'de tinta para pintar a parede'.format(altura,largura,area,tinta))