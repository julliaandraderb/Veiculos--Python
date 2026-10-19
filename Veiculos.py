
# Classe principal que representa um veículo
class Veiculo:
    def __init__(self, marca, modelo):
        # Atributos compartilhados pelos veículos
        self.marca = marca
        self.modelo = modelo

    # Método para ligar o veículo
    def ligar(self):
        print(f"O veículo {self.marca} {self.modelo} está ligado.")


# Classe Carro herda os atributos e métodos de Veiculo
class Carro(Veiculo):
    def __init__(self, marca, modelo, num_portas):
        # Inicializa os atributos da classe pai
        super().__init__(marca, modelo)

        # Atributo específico do carro
        self.num_portas = num_portas

    # Sobrescreve o método ligar da classe Veiculo
    def ligar(self):
        print(f"O carro {self.marca} {self.modelo} com {self.num_portas} portas está ligado.")


# Classe Moto também herda de Veiculo
class Moto(Veiculo):
    def __init__(self, marca, modelo, cilindradas):
        # Inicializa os atributos da classe pai
        super().__init__(marca, modelo)

        # Atributo específico da moto
        self.cilindradas = cilindradas

    # Sobrescreve o método ligar da classe Veiculo
    def ligar(self):
        print(f"A moto {self.marca} {self.modelo} está ligando com {self.cilindradas} cilindradas.")


# Cria um objeto da classe Carro
carro = Carro("Toyota", "Corolla", 4)

# Cria um objeto da classe Moto
moto = Moto("Honda", "CB 500", 500)

# Chama o método ligar de cada objeto
carro.ligar()
moto.ligar()
