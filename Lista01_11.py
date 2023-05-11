'''
11. Desenvolva um programa para calcular a venda de maçãs em uma banca de feira. O cliente compra maçãs custando R
$1,37 cada uma, mas caso ele compre a partir de uma dúzia pagará com desconto de 10%, portanto o valor da unidade
ficará por R $1,24. O programa deverá receber o número de maçãs desejadas pelo cliente, e retornar o valor total da
compra.
'''
qtd = int(input('Digite a quantidade de maças: '))
preco = 1.37
venda = preco*qtd
if qtd >= 12:
    venda *= 0.9
print(f'Valor total da compra foi de R${venda:.2f}')