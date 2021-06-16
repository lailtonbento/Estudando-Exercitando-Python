peso = float(input('Qual é o seu peso (kg): '))
altura = float(input('Qual é a sua altura (m): '))
imc = peso / (altura ** 2)
print('O seu IMC é {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso!')
elif 18.5 <= imc <= 25:
    print('Você está no seu peso ideal!')
elif 25 < imc <= 30:
    print('Você está em sobrepeso!')
elif 30 < imc <= 40:
    print('Você está em obesidade, cuidado!')
else:
    print('Você está em obesidade mórbida, TENHA CUIDADO!!')


