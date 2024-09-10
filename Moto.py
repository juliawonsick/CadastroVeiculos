from urllib.request import FancyURLopener
from Veiculo import Veiculo
# quando queremos herdar de uma superclase, classe mae/pai

class Moto(Veiculo):
    def __init__(self, marca,  modelo, placa, ano, cilindradas): #super init significa chamar o construtor da super classe
        super().__init__(marca, modelo, placa, ano) # cilindradas n é passado para asuperclasse  pois la na superclasse só tem esses, as cilindradas é específico da subclasse Moto
        self.__cilindradas = cilindradas
    def __str__(self):
        # invoco metodo __str__() da superclasse (Veiculo)
        # armazeno o retorno da variavel "retorno"
         retorno = super().__str__()
        # retorno a concatenação do valor da variavel 
        #"retorno" com as "__cilindradas"
         return f'''{retorno}
- Cilindradas: {self.__cilindradas}'''

        
 