''''
[FORBELLONE, 2022] Construa um algoritmo para calcular as raízes de uma equação do 2 grau (Ax² + Bx + C), sendo
que os valores A, B, C são fornecidos pelo usuário. (considere que a equação possui duas raízes reais).
'''
a, b, c = float(input()), float(input()), float(input())
delta = b ** 2 - 4 * a * c
if delta < 0:
    print('Raizes não tem definição nos reais.')
if delta >= 0:
    x1 = (-1*b + delta ** (1/2))/2 * a
    x2 = (-1*b - delta ** (1/2))/2 * a

print(f'As raízes da equação são: X1 = {x1:.2f} e X2 = {x2:.2f}')