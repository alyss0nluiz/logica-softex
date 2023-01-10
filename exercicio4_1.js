class Banco {
    constructor(conta, saldo, tipoConta, agencia) {
      this.conta = conta;
      this.saldo = saldo;
      this.tipoConta = tipoConta;
      this.agencia = agencia;
    }
  
    buscarSaldo() {
      return this.saldo;
    }
  
    deposito(valor) {
      this.saldo += valor;
      return `Depósito realizado com sucesso. Novo saldo: ${this.saldo}`;
    }
  
    saque(valor) {
      if (valor > this.saldo) {
        return "Saldo insuficiente para realizar saque.";
      } else {
        this.saldo -= valor;
        return `Saque realizado com sucesso. Novo saldo: ${this.saldo}`;
      }
    }
  
    numeroConta() {
      return this.conta;
    }
  }
  
  const minhaConta = new Banco(123456, 1000, 'corrente', 1234);
  console.log(minhaConta.buscarSaldo()); // 1000
  console.log(minhaConta.deposito(500)); // Depósito realizado com sucesso. Novo saldo: 1500
  console.log(minhaConta.saque(2000)); // Saldo insuficiente para realizar saque.
  console.log(minhaConta.numeroConta()); // 123456
  