
from Moto import Moto
from Veiculo import Veiculo

#instanciando a classe moto
falcon = Moto("Honda", "Falcon NX4", "abc", 2005, 400)
        #exibir uma info na tela =>
        # vai imprimir o RETORNO do  metodo (__str__)
print(falcon.__str__())

# instanciando a classe veiculo
cerato = Veiculo("Kia", "Cerato", "IRL", 2011)


print(cerato.__str__())


# abaixo estamos instanciando um obj da class veiculo
meuUno = Veiculo("Fiat", "Uno", "ABC-123", 2000)
print(meuUno.get_marca())
print(meuUno.calcularTempoUso())
meuUno.__ano = 2010
print(meuUno.calcularTempoUso())

teuFusca = Veiculo("Volks", "Fusca", "def235", 1995)

#print(meuUno.calcularTempoUso())
#print(teuFusca.calcularTempoUso())

#print("")
