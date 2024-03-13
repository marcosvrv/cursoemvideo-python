vcasa = float(input("Qual o valor da casa? R$" ))
salario = float(input("Qual o salário do comprador? R$"))
tempo = int(input("Quantos anos de financiamento? "))
prestacao = vcasa / (tempo * 12)
minimo = salario * 0.30

print("Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}".format(vcasa, tempo, prestacao))

if (prestacao <= minimo):
    print("Empréstimo pode ser CONCEDIDO")
else:
    print("Empréstimo NEGADO")