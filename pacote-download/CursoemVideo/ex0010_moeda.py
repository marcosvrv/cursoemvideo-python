r = float(input('Quanto dinheiro você tem na carteira? R$'))
d = r / 5.60
e = r / 6.60
print('Com {} você pode comprar US${:.2f} ou €{:.2f}'.format(r,d ,e))