soma = 0
contador = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        contador += 1
        soma = soma + c
print('A soma de todos os {} valores solicitados é {}'.format(contador, soma))
