# Fazer um programa que leia um numero e mostre, seu dobro, triplo e raiz quadrada

n = int (input('Digite um numero \n'))
dobro = n * 2
triplo = n * 3
rq = n**(1/2)
print('O numero digitado foi: \n{}\nO dobro de {} é \n{}\nO triplo de {} é:\n{}\nA raiz quadrada de {} é:\n{}'.format(n,n,dobro,n,triplo,n,rq))