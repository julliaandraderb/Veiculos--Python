# Atividade-Encapsulamento-de-Saldo-e-Hierarquia-de-Veículos
Exercicio 1
class ContaBancaria:
    def __init__(self, titular, numero_conta):
        self.titular = titular
        self.numero_conta = numero_conta
        self.__saldo = 0

    def get_saldo(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor} feito com sucesso.")
        else:
            print("Valor inválido para depósito.")

    def set_saldo(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R${valor} realizado.")
        else:
            print("Saldo insuficiente.")

    def consultar_saldo(self):
        print(f"Saldo atual: R${self.__saldo}")

    def exibir_extrato(self):
        print(f"Titular: {self.titular}")
        print(f"Número da Conta: {self.numero_conta}")
        print(f"Saldo: R${self.__saldo}")

conta1 = ContaBancaria("Majulle", "9888345697")
conta1.get_saldo(2000)
conta1.set_saldo(300)
conta1.consultar_saldo()
conta1.exibir_extrato()


Exercício 2
class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def ligar(self):
        print(f"O veículo {self.marca} {self.modelo} está ligado.")

class Carro(Veiculo):
    def __init__(self, marca, modelo, num_portas):
        super().__init__(marca, modelo)
        self.num_portas = num_portas

    def ligar(self):
        print(f"O carro {self.marca} {self.modelo} com {self.num_portas} portas está ligado.")

class Moto(Veiculo):
    def __init__(self, marca, modelo, cilindradas):
        super().__init__(marca, modelo)
        self.cilindradas = cilindradas

    def ligar(self):
        print(f"A moto {self.marca} {self.modelo} está ligando com {self.cilindradas} cilindradas.")

carro = Carro("Chevrolet", "Onix", 4)
moto = Moto("BMW", "Motorrad", 500)

carro.ligar()
moto.ligar()
