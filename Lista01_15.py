peso, altura = float(input('Peso (kg): ')), float(input('Altura (cm): '))
imc = peso / ((altura/100) ** 2)
if imc < 18.5:
    print('abaixo do peso')
elif imc < 25:
    print('peso normal')
elif imc < 30:
    print('acima do peso')
else:
    print('obeso')