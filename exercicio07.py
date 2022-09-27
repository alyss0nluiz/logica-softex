nome = (input("Digite o nome do aluno: "))
faltas = int(input("Digite o número de faltas do aluno: "))
nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno :"))
media = (nota1 + nota2) / 2

if media >= 7:
    print("O aluno: " + nome + " foi aprovado por média: " , media , " !")
else:
    print("O aluno: " + nome + " foi reprovado por média: " , media , " !")
if faltas <=3 and media >= 7:
    print("O aluno: " + nome + " foi aprovado!")
else:
    print("O aluno: " + nome + " foi reprovado por falta!")