#Digite um valor e que ele seja acrescido de 15%

salario = float(input('Digite o valor do salário:'))
porcentagem = salario * (15/100)
novosalario = salario + porcentagem
print('Seu salário sem aumento é : {}\nSeu novo salário com 15% de aumento é de : {}'.format(salario,novosalario))