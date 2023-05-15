'''
Escrever um algoritmo que leia uma quantidade desconhecida de números e conte quantos deles estão nos seguintes
intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deve terminar quando for lido um número negativo.
'''
cont1 = cont2 = cont3 = cont4 = 0
while (True):
    valor = int(input('Digite valor entre 0 e 100: '))
    if valor < 0:
        break
    if valor >0 and valor <=25:
        cont1 += 1
    elif valor <= 50:
        cont2 += 1
    elif valor <= 75:
        cont3 += 1
    elif valor <=100:
        cont4 += 1
print(f'Quantidade no intervalo [0-25]: {cont1}')
print(f'Quantidade no intervalo [26-50]: {cont2}')
print(f'Quantidade no intervalo [51-75]: {cont3}')
print(f'Quantidade no intervalo [76-100]: {cont4}')


