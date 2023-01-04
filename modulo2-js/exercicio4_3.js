const lang = ["j", "a", "v", "a", "s", "c", "r", "i", "p", "t"];

const jogador = {
    Nome: 'Neymar',
    Posicao: 'PE',
    Nacionalidade: 'Brasileiro'
}

function estudo(){
    console.log("\nQual linguagem de programção estou estudando agora?");
    for (const e of lang) {
        console.log(e);
    }
}

function jogador(){
    console.log("\nDados do jogador:\n")
    for (const index in jogador){
        console.log(`${index} : ${jogador[index]}`)
    }
}

estudo()

jogador()