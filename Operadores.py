n1= int (input('Digite um número'))
n2 = int (input('Digite outro número'))
s = n1 + n2
m = n1 * n2
di = n1 // n2
d = n1 / n2
p1 = n1**2
print('O resultado da soma é {}:'.format(s))
print('O resultado da multiplicação é {}:'.format(m))
print ('O resultado da divisão inteira : {}'.format(di))
# Exemplo de formatação de casas decimais
print('O resultado da divisão com resto {:.3f}'.format(d))
print('O resultado da potenciação é: {}'.format(p1))
print ('O resultado da potenciação é  : \n{} da multiplicação é :\n {} da divisão inteira \n{} da divisão com resto \n{} da potenciação \n{}'.format(s,m,di,d,p1))
