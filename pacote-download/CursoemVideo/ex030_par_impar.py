numero = int(input('Me diga um número qualquer: '))
resultado = numero % 2
if resultado == 1:
    print('O número {} é ímpar'.format(numero))
else:
    print('O número {} é par'.format(numero))