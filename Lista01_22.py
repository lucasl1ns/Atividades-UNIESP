'''
Desenvolver um algoritmo que leia a altura de 15 pessoas. Este programa deverá calcular e mostrar :
a. A menor altura do grupo;
b. A maior altura do grupo;
'''
for i in range (1, 16):
    altura = int(input('Digite a idade: '))
    if i == 1:
        maior = altura
    else:
        if altura > maior:
            maior = altura
print(f'A maior idadade é : {maior}')