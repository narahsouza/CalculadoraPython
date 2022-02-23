print('\nCalculadora')
ms = 0
while True:
    print('\nMemória armazenada(MS) = ', ms)
    print('\nO que você deseja fazer?')
    operador = input('\n1-Somar / 2-Subtrair / 3-Multiplicar / 4-Dividir / 0-Sair: ')
    if operador == "0":
        break
    valor_1 = float(input('\nInsira o primeiro número: '))
    valor_2 = float(input('\nInsira o segundo número: '))
    if operador == "1":
        resultado = valor_1 + valor_2
        print('\nResultado = ', resultado)
    elif operador == "2":
        resultado = valor_1 - valor_2
        print('\nResultado = ', resultado)
    elif operador == "3":
        resultado = valor_1 * valor_2
        print('\nResultado = ', resultado)
    elif operador == "4":
        resultado = valor_1 / valor_2
        print('\nResultado = ', resultado)
    else:
        operador = None
        print('\nOperadoração inválida.')
        input('\nPressione qualquer tecla para encerrar.')
        break
    print('\nDeseja armazenar o resultado (MS)?')
    memoria = input('\n1-Somar (M+) / 2-Subtrair (M-) / "Enter"-Não Armazenar / 0-Sair: ')
    if memoria == '1':
        ms += resultado
    elif memoria == '2':
        ms -= resultado
    elif memoria == '':
        continue
    elif memoria == '0':
        break
    else:
        nome = None
        print('\nEntrada invalida, o valor não foi salvo.')
        continue
