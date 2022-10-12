class Conta:

    total_contas = 0

    def __init__(self,saldo):
        self.saldo = saldo
        Conta.total_contas += 1

    def deposita(self,valor):
        self.saldo += valor

print("\n----- Poupança com Python -----")
c1 = Conta(float(input('\nDigite o valor do saldo inicial da sua poupança: ')))
print(f'\nVocê está efetuando um depósito na conta nº {c1.total_contas}')
c1.deposita(float(input('\nQuanto você deseja depositar?: ')))
print("\nSeu saldo é de R$",c1.saldo)

c2 = Conta(float(input('\nDigite o valor do saldo inicial da sua poupança: ')))
print(f'\nVocê está efetuando um depósito na conta nº {c2.total_contas}')
c2.deposita(float(input('\nQuanto você deseja depositar?: ')))
print("\nSeu saldo é de R$",c2.saldo)

c3 = Conta(float(input('\nDigite o valor do saldo inicial da sua poupança: ')))
print(f'\nVocê está efetuando um depósito na conta nº {c3.total_contas}')
c3.deposita(float(input('nQuanto você deseja depositar?: ')))
print("\nSeu saldo é de R$",c3.saldo)