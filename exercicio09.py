import time

inicioTempo = int(input("Insira o valor em segundos para detonar o explosivo: "))

print("Iniciando contagem regressiva...")
for i in range(inicioTempo,0,-1):
    print(i)
    time.sleep(1)
print("Boomm!!")