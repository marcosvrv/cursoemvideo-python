from time import sleep 

valor1 = int(input('Primeiro valor: '))
valor2 = int(input('Segundo valor: '))

opcao = 0

while opcao != 5:
    print('''\nEscolha uma das opções abaixo: 
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa\n''')

    opcao = int(input('Qual é a sua opção? '))

    if opcao == 1:
        soma = valor1 + valor2
        print('A soma entre {} + {} é igual a {}.'.format(valor1, valor2, soma))
    elif opcao == 2:
        produto = valor1 * valor2
        print('O resultado de {} x {} é igual a {}.'.format(valor1, valor2, produto))
    elif opcao == 3:
        if valor1 > valor2:
            maior = valor1
        else:
            maior = valor2
        print('Entre {} e {}, o maior valor é {}.'.format(valor1, valor2, maior))
    elif opcao == 4:
        print('Informe os números novamente: ')
        valor1 = int(input('Primeiro valor: '))
        valor2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
        sleep(1)
    sleep(1)
print('Fim do programa. Volte sempre!')