from abc import ABC, abstractmethod
class Veiculo(ABC):
    def __init__(self, marca, modelo,  ano):
        self.__marca=marca
        self.__modelo=modelo
        self.__ano=ano
        
    def getMarca(self):
        return self.__marca
    def getModelo(self):
        return self.__modelo
    def getAno(self):
        return self.__ano
    def setMarca(self, marca):
        self.__marca=marca
    def setmodelo(self, modelo):
        self.__modelo=modelo
    def setano(self, ano):
        self.__ano=ano
       
    @abstractmethod
    def mostar(self):
        pass 
        