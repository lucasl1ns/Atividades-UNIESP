'''
25. Faça um algoritmo estruturado que leia uma quantidade não determinada de números positivos. Calcule a quantidade de
números pares e ímpares, a média de valores pares e a média geral dos números lidos. O número que encerrará a leitura
será zero.
'''
cont_par = cont_impar = soma_par = soma_impar = 0
while(True):
    numero = int(input())
    if numero == 0:
        break
    if numero % 2 == 0:
        cont_par += 1
        soma_par += numero
    else:
        cont_impar += 1
        soma_impar += numero
media_par = soma_par / cont_par
media = (soma_par + soma_impar) / (cont_par + cont_impar)

print(f'Foram informados {cont_par} números pares.')
print(f'Foram informados {cont_impar} números ímpares.')
print(f'A média dos valores pares é {media_par:.2f}.')
print(f'A média global dos valores informados é {media:.2f}')


