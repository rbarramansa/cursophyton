#Crie um programa que leia o nome da cidade e apresente True caso o nome comece com santo, ou false caso não

cidade = str(input('Digite o nome de uma cidade')).strip()
cidadedividido = cidade.split()
print('Se o nome da cidade começar com santo, informar {}'.format(cidadedividido[0] in 'santo'))