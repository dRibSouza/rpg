from ContaBancaria import ContaBancaria


class ContaEspecial(ContaBancaria):
    def bajular_cliente(self):
        print("O senhor gostaria de um cafézinho?")


Klismann = ContaBancaria("klismann", 0)

cliente_indra = ContaEspecial("Indra Company", 12000.83)

cliente_indra.consultar_saldo()

cliente_indra.depositar(30000.00)

cliente_indra.consultar_saldo()

cliente_indra.sacar(12000.83)

cliente_indra.consultar_saldo()

Klismann.consultar_saldo()
