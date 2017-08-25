velocidade = float(input('Digite a km'))


if velocidade > 80.0:
    multa = (velocidade - 80.0)
    valormulta = multa * 7.0
    print('Você foi multado, o valor da multa foi {}'.format(valormulta))

else:
    print('Parabéns vc andou no limite recomendado pela pista')