x = 0
y = 0
z = 0
nulo = 0

stop = False
while stop == False:

    stop_voto = False
    print("--- Urna Eleitoral com Python ---")
    print("\nEm qual candidato você deseja votar: ")
    print("\nCandidato X = 889")
    print("\nCandidato Y = 847")
    print("\nCandidato Z = 515")
    print("\nBranco ou nulo = 0")
    
    try:
        voto = int(input("\nEm qual Candidato você deseja votar: "))

        def votacao(voto):
            if (voto == 889):
                res = "Candidato X"
            elif (voto == 847):
                res = "Candidato Y"
            elif (voto == 515):
                res = "Candidato Z"
            else:
                res = "Branco ou Nulo"
            return res

        contagem = votacao(voto)

        if (contagem == "Candidato X"):
            x = (x + 1)
        elif (contagem == "Candidato Y"):
            y = (y + 1)
        elif (contagem == "Candidato Z"):
            z = (z + 1)
        else:
            nulo = (nulo + 1)

        stop_confirmacao = False
        while stop_confirmacao == False:
            print("\nVocê votou em: ",contagem,"!!!")
            encerrar_votacao = str (input("\nDeseja encerrar a votação?? [s/n]: "))
            if (encerrar_votacao == "s"):
                stop = True
                stop_confirmacao = True
                print("\nVotação encerrada!!!")
            elif (encerrar_votacao == "n"):
                stop_confirmacao = True
            else:
                print("\nOpção invalida!!!")
                print("\nResponda novamente!!")
    except:
        print("\nResposta invalida!!!")
        print("\nVote novamente!!")

if (x > y) and (x > z):
    print("\nO candidato eleito foi X!!!")
elif (y > x) and (y > z):
    print("\nO candidato eleito foi Y!!!")
elif (z > x) and (z > y):
    print("\nO candidato eleito foi Z!!!")
else:
    print("\nA votação deu empate!!!")

print("\n---- Resultado da apuração ----")
print("\nO candidato X teve", x,"voto(s) no total!!!")
print("O candidato Y teve", y,"voto(s) no total!!!")
print("O candidato Z teve", z,"voto(s) no total!!!")
print("Brancos e nulos somaram um total de", nulo,"voto(s)!!!")