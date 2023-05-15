'''
23. Desenvolver um algoritmo que leia um número não determinado de valores e calcule e escreva a média aritmética dos
valores lidos, a quantidade de valores positivos, a quantidade de valores negativos e o percentual de valores negativos e
positivos.
'''
pos = neg = qtd = soma = 0
while(True):
    valor = int(input('Digite um número: '))
    qtd += 1
    soma += valor
    if valor >= 0:
        pos += 1
    else:
        neg += 1
    media = soma / qtd
    print(f'Média = {media:.2f} | Qtd Positivo: {pos} | Qtd Negativo: {neg} | % Positivo = {(pos/qtd)*100}% | % Positivo = {(neg/qtd)*100}%')

