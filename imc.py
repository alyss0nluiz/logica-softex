def calculadoraIMC(peso,altura):
    imc = peso/(altura*altura)
    if(imc <= 18.5):
        return "Magreza"
    elif(imc > 18.5) and (imc <= 24.9):
        return "Saudável"
    elif(imc >= 25) and (imc <= 29.9):
        return "Sobrepeso"
    elif(imc >= 30) and (imc <= 34.9):
        return "Obesidade grau 1"
    elif(imc >= 35) and (imc <= 39.9):
        return "Obesidade severa grau 2"
    else:
        return "Obesidade morbida grau 3"

peso = float(input("Insira seu peso: "))
altura = float(input("Insira a sua altura: "))
resultado = calculadoraIMC(peso,altura)
print("Seu IMC é: ", resultado)