sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
'''while sexo not in 'MF':'''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]