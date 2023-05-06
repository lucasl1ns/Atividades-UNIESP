altura, peso = float(input('Altura(m): ')), float(input('Peso(kg): '))
imc = peso / (altura ** 2 )
print(f'O IMC é : {imc:.2f}')