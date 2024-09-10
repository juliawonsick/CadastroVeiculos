from Veiculo import Veiculo
class Caminhao(Veiculo):
    def __init__(self, marca, modelo, placa, ano, capacidade):
        super().__init__(marca, modelo, placa, ano)
        self.__capacidade = capacidade
    #Override - Sobescrever o método _str_()
    def _str_(self):
        ret = super()._str_()
        return f''' {ret}
- Capacidade {self.__capacidade}'''