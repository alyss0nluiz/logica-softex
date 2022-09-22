programa
{
	
	funcao inicio()
	{
		logico condicao

		escreva("É terrestre:?")
		leia(condicao)
		se(condicao == verdadeiro) {
			escreva("Cabe apenas uma pessoa:?")
			leia(condicao)
			se(condicao == verdadeiro) {
				escreva("É pesado:?")
				leia(condicao)
				se(condicao == verdadeiro) {
					escreva("O veículo é um trator!")
				}senao {
					escreva("O veículo é uma bicicleta!")
				}
			}senao {
				escreva("Usa capacete:?")
				leia(condicao)
				se(condicao == verdadeiro) {
					escreva("O veículo é uma moto!")
				}senao {
					escreva("Tem passageiro:?")
					leia(condicao)
					se(condicao == verdadeiro) {
						escreva("Usa trilho:?")
						leia(condicao)
						se(condicao == verdadeiro) {
							escreva("O veículo é um trem!")
						}senao {
							escreva("É alto:?")
							leia(condicao)
							se(condicao == verdadeiro) {
								escreva("Usa carroceria:?")
								leia(condicao)
								se(condicao == verdadeiro){
									escreva("O veículo é um caminhão!")
								}senao {
									escreva("O veículo é um ônibus!")
								}
							}senao {
								escreva("O veículo é um carro!")
							}
						}
					}
				}
			}
		}senao {
			escreva("É aéreo:?")
			leia(condicao)
			se(condicao == verdadeiro) {
				escreva("Precisa pular:?")
				leia(condicao)
				se(condicao == verdadeiro) {
					escreva("O veículo é asa delta!")
				}senao {
					escreva("É devagar:?")
					leia(condicao)
					se(condicao == verdadeiro) {
						escreva("O veículo é um balão!")
					}senao {
						escreva("Possui asas fixas:?")
						leia(condicao)
						se(condicao == verdadeiro) {
							escreva("O veículo é um avião!")
						}senao {
							escreva("O veículo é um helicóptero!")
						}
					}
				}
			}senao {
				escreva("É aquático:?")
				leia(condicao)
				se(condicao == verdadeiro) {
					escreva("É coberto d'água:?")
					leia(condicao)
					se(condicao == verdadeiro) {
						escreva("O veículo é um Submarino!")
					}senao {
						escreva("Possui vela:?")
						leia(condicao)
						se(condicao == verdadeiro) {
							escreva("O veículo é um barco!")
						}senao {
							escreva("É alto:?")
							leia(condicao)
							se(condicao == verdadeiro) {
								escreva("O veículo é um navio!")
							}senao {
								escreva("O veículo é uma lancha!")
							}
						}
					}
				}
			}
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 2293; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */