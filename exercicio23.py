class pessoa():
    def __init__(self,nome,peso):
        self._nome = nome
        self._peso = peso

    def exibir(self):
        print("\nMeu nome é",self._nome,"e eu ganhei",self._peso,"kg no último ano!!")
        print("-----------------------------------------------------------------------------------")

    def set_peso(self,novo_peso):
        self._peso -= novo_peso

    def get_nome(self):
        return self._nome

    def get_peso(self):
        return self._peso

print("--------- Balança Python ---------")
p1 = pessoa(input('\nQual o seu nome completo?: '),float(input('\nQual o seu peso atual?: ')))
p1.get_nome()
p1.get_peso()
p1.set_peso(float(input('\nQuantos kg você tinha ano passado?: ')))
p1.get_nome()
p1.get_peso()
p1.exibir()

p2 = pessoa(input('\nQual o seu nome completo?: '),float(input('\nQual o seu peso atual?: ')))
p2.get_nome()
p2.get_peso()
p2.set_peso(float(input('\nQuantos kg você tinha ano passado?: ')))
p2.get_nome()
p2.get_peso()
p2.exibir()