valor, per = float(input('Preço: R$')), float(input('Percentual do desconto(%): '))
desconto = (per/100) * valor
valor_final = valor - desconto
print(f'Valor final: R${valor_final:.2f}')