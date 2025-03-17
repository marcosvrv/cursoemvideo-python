from random import randint
from time import sleep

# Computador sorteia um número entre 0 e 10
computador = randint(0, 10)

print('-=' * 30)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=' * 30)

# Inicializa variáveis
palpites = 0
acertou = False

# Loop até o jogador acertar
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    print('PROCESSANDO...')
    sleep(1)

    if jogador == computador:
        print('Parabéns! Você acertou o número {}.'.format(computador))
        print('Você precisou de {} palpites para vencer.'.format(palpites))
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente um número maior.')
        else:
            print('Menos... Tente um número menor.')