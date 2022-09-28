def calc(num1,num2,operador):
    if operador == 1:
        print(f'Resultado: {num1+num2}')
    elif operador == 2:
        print(f'Resultado: {num1-num2}')
    elif operador == 3:
        print(f'Resultado: {num1*num2}')
    elif operador == 4:
        print(f'Resultado: {num1/num2}')
    else:
        print('0')

print("Escolha a operação que deseja realizar: ")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

operador = int(input("Operação: "))
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

calc (num1, num2, operador)