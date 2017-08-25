#Desenvolva um programa que pergunte a km de uma viagem em km
#E calcule o preço da passagem , cobrando 0.50 por km para viagem de até 200 KM
#E 0.45 para viagens mais longas.

km = float(input('Digite a km a ser percorrida'))
if km <= 200:
    print(km * 0.50)
else:
    print(km*0.45)