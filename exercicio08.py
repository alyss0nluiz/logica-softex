rodas = int(input("Insira a quantidade de rodas do veículo: "))
pesoBruto = float(input("Insira o peso bruto do veículo: "))
quantPessoas = int(input("Insira a quantidade de pessoas no veículo: "))

if rodas <= 3:
    print("A melhor categoria de habilitação para o veículo informado é: A")
elif rodas >= 4 and quantPessoas >= 8:
    print("A melhor categoria de habilitação para o veículo informado é: D")
elif rodas == 4 and pesoBruto <= 3500:
    print("A melhor categoria de habilitação para o veículo informado é: B")
elif rodas >= 4 and (pesoBruto >= 3500 and pesoBruto <= 6000):
    print("A melhor categoria de habilitação para o veículo informado é: C")
else:
    print("A melhor categoria de habilitação para o veículo informado é: E")