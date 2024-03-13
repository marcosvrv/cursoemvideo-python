distancia = float(input('Qual a distância da sua viagem? '))
print('Você está prestes a começãr uma viagem de {} Km.'.format(distancia))
if distancia <=200:
    valor = distancia * 0.50
else:
    valor = distancia * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(valor))

