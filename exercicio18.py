class calculo:
    def __init__(self):
            self.n1 = 0
            self.n2 = 0
            self.n3 = 0
    def soma(self):
            return self.n1 + self.n2 + self.n3
    def subtracao(self):
            return self.n1 - self.n2 - self.n3
    def multiplicacao(self):
            return self.n1 * self.n2 * self.n3
    def divisao(self):
            return self.n1 / self.n2 / self.n3

calc = calculo()
calc.n1 = int(input("\nInsira o primeiro número complexo: "))
calc.n2 = int(input("\nInsira o segundo número complexo: "))
calc.n3 = int(input("\nInsira o terceiro número complexo: "))

print("\n----- Resultados das operações básicas -----")
print("\nSoma = ", calc.soma())
print("Subtração = ", calc.subtracao())
print("Multiplicação = ", calc.multiplicacao())
print("Divisão = ", calc.divisao())

print("\n----- Propiedades real e imag dos numerais -----")
print('\n',[calc.n1.real])
print('',[calc.n1.imag])
print('\n',[calc.n2.real])
print('',[calc.n2.imag])
print('\n',[calc.n3.real])
print('',[calc.n3.imag])