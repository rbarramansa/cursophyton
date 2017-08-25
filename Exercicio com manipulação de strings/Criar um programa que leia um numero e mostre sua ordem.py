#Crie um programa que leia um numero e mostre a sua ordem
#Ex:1234
#Unidade :4
#Dezena:3
#Centena:2
#Milhar:1

num = int(input('Digite um numero'))
u = num//1 % 10
d = num//10 % 10
c = num//100 % 10
m = num//1000 % 10

print('A unidade digitada foi {}'.format(u))
print('A dezena digitada foi {}'.format(d))
print('A centena digitada foi {}'.format(c))
print('A milhar digitada foi {}'.format(m))