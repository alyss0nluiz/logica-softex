print("------- Tratamento de Nomes com Python -------")
nome = str(input("\nInsira o seu nome completo: ")).strip()
print('\nAnalisando seu nome...')

primeiroNome = nome.split()
print(f'\nO seu primeiro nome contém {len(primeiroNome[0])} letras!!')

semEspaco = len(nome) - nome.count(' ')
print(f'\nSeu nome tem ao todo {semEspaco} letras!!')

totalLetras = input("\nDeseja saber quantas vezes determinada letra aparece em seu nome? [s/n]: ")
if (totalLetras == 's'):
    letra = str(input('\nQual letra você deseja saber quantas vezes aparece em seu nome? '))
    print(f"\nVocê escolheu a letra {letra.upper()} e a mesma aparece {nome.count(letra)} vezes no seu nome")
else:
    exit()