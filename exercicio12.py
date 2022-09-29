stop = False
while stop == False:
    try:
        nome = str (input("\nInsira seu nome completo: "))
        idade = int (input("\nInsira sua data de nascimento: "))
        if (idade >= 1922) and (idade <= 2021):
            idade = 2022 - idade
            print("\n" + nome + " tem ", idade ," anos ou irá completar em 2022!!")
            stop = True
    except:
        print("\nOs dados inseridos são invalidos!!")
        print("\nInsira seus dados novamente!!")