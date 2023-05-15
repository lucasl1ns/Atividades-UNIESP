'''
Escreva um algoritmo que leia um valor inicial A e imprima a sequência de valores do cálculo de A! e o seu resultado.
Ex: 5! = 5 X 4 X 3 X 2 X 1 = 120
'''
a = int(input())
prod = 1
for i in range (a, 1, -1):
    prod *= i
print(prod)