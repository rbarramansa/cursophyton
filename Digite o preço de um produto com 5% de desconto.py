#Faça um programa que leia o preço de um produto e mostre seu novo preço com 5% de desconto

preco = float(input('Digite o preço\n'))
porcentagem = (preco * (5/100))
desconto = preco - porcentagem
print('O preço digitado sem desconto foi:\n{}\nO valor com 5% de desconto é de :\n{}'.format(preco,desconto))

