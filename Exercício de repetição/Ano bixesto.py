#Crie um programa que leia uo ano e diga se ele é bixesto ou não

ano = int(input('Digite o ano'))

if ano % 4 == 0 and ano % 100 !=0 :
    print('O ano de {} é bixesto'.format(ano))

else:
    print('O ano não é bixesto')