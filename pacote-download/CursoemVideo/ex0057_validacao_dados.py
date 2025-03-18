sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
'''while sexo != 'M' and sexo != 'F':'''
while sexo not in 'MF':   
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: '))