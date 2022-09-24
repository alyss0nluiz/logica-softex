programa
{

	cadeia melhorNotaA, melhorNotaB, melhorNotaC, melhorNotaD, aluno
	
	funcao inicio()
	{
		inteiro contador, aprovadosA = 0, aprovadosB = 0, aprovadosC = 0, aprovadosD = 0, aprovados
		cadeia nomeA, nomeB, nomeC, nomeD
		real notaA, notaB, notaC, notaD, mnA = 0.0, mnB = 0.0, mnC = 0.0, mnD = 0.0, maiorNota

		para(contador = 1; contador <=25; contador ++) {
			escreva("Digite o nome do aluno: ", contador, "º da turma A: ")
			leia(nomeA)
			escreva("Digite a nota do aluno ", contador, "º da turma A: ")
			leia(notaA)
			se(notaA < 0 ou notaA > 10) {
				escreva("Nota inválida!\nDigite uma nota entre 0 a 10: ")
				leia(notaA)
			}se(notaA >= 7) {
				aprovadosA = aprovadosA+1
			}
			se(notaA > mnA) {
				mnA = notaA
				melhorNotaA = nomeA
			}
		}
		escreva("\n")
		escreva("-------------------------------------------------------")
		escreva("\n")
		para(contador = 1; contador <=25; contador ++) {
			escreva("Digite o nome do aluno: ", contador, "º da turma B: ")
			leia(nomeB)
			escreva("Digite a nota do aluno ", contador, "º da turma B: ")
			leia(notaB)
			se(notaB < 0 ou notaB > 10) {
				escreva("Nota inválida!\nDigite uma nota entre 0 a 10: ")
				leia(notaB)
			}se(notaB >= 7) {
				aprovadosB = aprovadosB+1
			}
			se(notaB > mnB) {
				mnB = notaB
				melhorNotaB = nomeB
			}
		}
		escreva("\n")
		escreva("-------------------------------------------------------")
		escreva("\n")
		para(contador = 1; contador <=25; contador ++) {
			escreva("Digite o nome do aluno: ", contador, "º da turma C: ")
			leia(nomeC)
			escreva("Digite a nota do aluno ", contador, "º da turma C: ")
			leia(notaC)
			se(notaC < 0 ou notaC > 10) {
				escreva("Nota inválida!\nDigite uma nota entre 0 a 10: ")
				leia(notaC)
			}se(notaC >= 7) {
				aprovadosC = aprovadosC+1
			}
			se(notaC > mnC) {
				mnC = notaC
				melhorNotaC = nomeC
			}
		}
		escreva("\n")
		escreva("-------------------------------------------------------")
		escreva("\n")
		para(contador = 1; contador <=25; contador ++) {
			escreva("Digite o nome do aluno: ", contador, "º da turma D: ")
			leia(nomeD)
			escreva("Digite a nota do aluno ", contador, "º da turma D: ")
			leia(notaD)
			se(notaD < 0 ou notaD > 10) {
				escreva("Nota inválida!\nDigite uma nota entre 0 a 10: ")
				leia(notaD)
			}se(notaD >= 7) {
				aprovadosD = aprovadosD+1
			}
			se(notaD > mnD) {
				mnD = notaD
				melhorNotaD = nomeD
			}
		}

		se(mnA > mnB e mnA > mnC e mnA > mnD) {
			maiorNota = mnA
			aluno = melhorNotaA
		}
		se(mnB > mnA e mnB > mnC e mnB > mnD) {
			maiorNota = mnB
			aluno = melhorNotaB
		}
		se(mnC > mnA e mnC > mnB e mnC >mnD) {
			maiorNota = mnC
			aluno = melhorNotaC
		}
		se(mnD > mnA e mnD > mnB e mnD > mnC) {
			maiorNota = mnD
			aluno = melhorNotaD
		}

		aprovados = aprovadosA + aprovadosB + aprovadosC + aprovadosD

		escreva("----------------------------------------\n")
		escreva("---------------Resultados---------------")
		escreva("\nA quantidade de alunos aprovados na turma A foi: ", aprovadosA)
		escreva("\nA maior nota da turma A foi: ", mnA)
		escreva("\nO melhor aluno da turma A foi: ", melhorNotaA)
		escreva("\nA quantidade de alunos aprovados na turma B foi: ", aprovadosB)
		escreva("\nA maior nota da turma B foi: ", mnB)
		escreva("\nO melhor aluno da turma B foi: ", melhorNotaB)
		escreva("\nA quantidade de alunos aprovados na turma C foi: ", aprovadosC)
		escreva("\nA maior nota da turma C foi: ", mnC)
		escreva("\nO melhor aluno da turma C foi: ", melhorNotaC)
		escreva("\nA quantidade de alunos aprovados na turma D foi: ", aprovadosD)
		escreva("\nA maior nota da turma D foi: ", mnD)
		escreva("\nO melhor aluno da turma D foi: ", melhorNotaD)
		escreva("\nA maior nota foi a do(a) aluno(a) ", aluno)
		escreva("\nO total de alunos aprovados foi de: ", aprovados)
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 3827; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */