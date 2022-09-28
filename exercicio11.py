def calc(operador, num1,num2):
    if operador == 1:
        print(f'\nResultado: {num1+num2}')
    elif operador == 2:
        print(f'\nResultado: {num1-num2}')
    elif operador == 3:
        print(f'\nResultado: {num1*num2}')
    elif operador == 4:
        print(f'\nResultado: {num1/num2}')

operador = 1

while operador:
    print("\nEscolha a operação a ser realizada: ")
    print("1: Soma")
    print("2: Subtração")
    print("3: Multiplicação")
    print("4: Divisão")
    print("0: Sair!!")
    operador = int(input('\nOperador: '))
    if operador == 0:
        print("\nCalculadora encerrada!!")
        exit()
    elif 1 <= operador <= 4:
        num1 = float(input("Insira o primeiro número: "))
        num2 = float(input("Insira o segundo número: "))

        calc(operador, num1, num2)
    else:
        print("\nOperação Invalida!!")