import random

def advinha(x):
    numero_aleatorio = random.randint(1,x)
    advinhe = 0
    while advinhe != numero_aleatorio:
        advinhe = input(f'Advinha um numero entre 1 e {x}')
        if advinhe < numero_aleatorio:
            print('Tente novamente,\nInsira um numero maior.')
        elif advinhe > numero_aleatorio:
            print('Tente novamente,\nInsira um numero menor.')
    print(f'Parabens, você acertou o numero {numero_aleatorio}.')

def computador_advinha(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            advinhe =random.randint(low, high)
        else:
            advinhe = low            
        feedback = input(f'Chuto {advinhe}, muito alto? (H), muito baixo? (L), ou correto? (C). ')
        if feedback == 'h':
            high = advinhe - 1
        elif feedback == 'l':
            low = advinhe + 1

    print(f'O computador advinhou seu numero {advinhe},corretamente.')

computador_advinha(25)