n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer em te cohecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))



