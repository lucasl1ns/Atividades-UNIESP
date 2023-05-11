rep = 1
while (rep<11):
    print(f'\033[1mTABUADA DE {rep}\033[0m')
    for i in range (1, 11):
        print(f'{i} x {rep} = {i * rep}')
    print()
    rep +=1