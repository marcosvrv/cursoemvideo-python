peso = float(input('Qual o seu peso? (KG) '))
altura = float(input('Qual a sua altura? (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('\033[31mVocê está abaixo do peso normal.\033[m')
elif 18.5 <= imc <25:
    print('\033[32mVocê está na faixa de peso normal.\033[m')
elif 25 <= imc < 30:
    print('\033[33mVocê está em sobrepeso.\033[m')
elif 30 <= imc < 40:
    print('\033[31mVocê está em obesidade.\033[m')
elif imc >= 40:
    print('\033[41mVocê está em obesidade mórbida.\033[m')