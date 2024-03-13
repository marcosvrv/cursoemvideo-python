print('\033[31m-=\033[m'*20)
print('Analisador de Triângulos')
print('\033[31m-=\033[m'*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo', end='')
    if r1 == r2 == r3:
        print(' \033[32mEQUILÁTERO\033[m')
    elif r1 != r2 != r3 != r1:
        print(' \033[32mESCALENO\033[m')
    else:
        print(' \033[32mISÓSCELES\033[m')

else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')