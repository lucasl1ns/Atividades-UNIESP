'''
12. Um programa é necessário para habilitar o funcionamento de uma conta corrente em um banco digital. O programa deve
permitir ao cliente iniciar com um depósito, realizar um saque, e ao final verificar se o saldo da conta está positivo ou
negativo. Se negativo, informa qual o valor será necessário para quitar o débito.
'''
deposito = float(input('Valor do depósito: R$'))
saque = float(input('Valor do saque: R$'))
saldo = deposito - saque
if saldo < 0:
    print('Saldo negativo!')
    print(f'Para quitar o débito é necessário depositar R${abs(saldo):.2f}')
else:
    print('Saldo positivo')