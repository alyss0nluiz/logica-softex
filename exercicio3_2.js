// Função tradicional sem parâmetros
function mostrarMensagem() {
    console.log("Bem-vindo à calculadora!");
}

// Função tradicional com parâmetros e retorno de valor
function somar(x, y) {
    return x + y;
}

// Arrow function com parâmetros e retorno de valor
const multiplicar = (x, y) => x * y;

// Utilizando as funções
mostrarMensagem();
let resultado = somar(3, 4);
console.log(resultado);
resultado = multiplicar(3, 4);
console.log(resultado);
