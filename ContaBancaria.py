class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if (valor > self.saldo):
            print("Não é possível sacar esse valor, seu saldo é insuficiente.")
        else:
            self.saldo -= valor

    def consultar_saldo(self):
        print(f"Saldo atual: R${self.saldo:2f}")


# danilo = ContaBancaria(titular="Danilo", saldo=0)

# danilo.depositar(10)
# danilo.consultar_saldo()

# danilo.sacar(15)
# danilo.sacar(10)
# danilo.consultar_saldo()
