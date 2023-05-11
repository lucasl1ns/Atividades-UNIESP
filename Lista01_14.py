a, b = int(input('Valor de A: ')), int(input('Valor de B: '))
operacao = input('Qual operação deseja fazer entre A e B: ')
if operacao == '+':
    op = 'soma'
    conta = a + b
elif operacao == '-':
    op = 'subtração'
    conta = a - b
elif operacao == '*':
    op = 'produto'
    conta = a * b
elif operacao == '/':
    op = 'divisão'
    conta = a / b
elif operacao == '**':
    op = 'potenciação'
    conta = a ** b

print(f'A operação escolhida foi {op.upper()} e o resultado é {a} {operacao} {b} = {conta:.2f}')