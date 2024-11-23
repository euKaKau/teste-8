from veiculo import Veiculo
class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, nPortas):
      super().__init__(marca, modelo, ano)
      self.__nPortas=nPortas
      
    def setnPortas(self, portas):
        self.__nPortas=portas
    def getnPortas(self):
        return self.__nPortas
    def mostar(self):
        return (f"O carro da marca: {self.getMarca()}, Modelo {self.getModelo()}, Ano: {self.getAno()}, e Portas: {self.getnPortas()} ")
    
        
