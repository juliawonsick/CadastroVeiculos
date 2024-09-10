from Veiculo import Veiculo
class Carro(Veiculo):
    def __init__(self, marca, modelo, placa, ano, n_portas):
        super().__init__(marca, modelo, placa, ano)
        self.__n_portas = n_portas 
    # override - sobrescrever o metodo __str__()
    def __str__(self):
        ret =  super().__str__()
        return f'''{ret}
- Número de portas {self.__n_portas}'''

