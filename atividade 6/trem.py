from veiculo import Veiculo
class Trem(Veiculo):
    def __init__(self, marca, modelo, ano, nVagoes):
        super().__init__(marca, modelo, ano)
        self.__nVagoes=nVagoes
        
    def setnVagoes(self, vagoes):
        self.__nVagoes=vagoes
    def getnVagoes(self):
        return self.__nVagoes
    
    def mostar(self):
        return (f"O trem da marca: {self.getMarca()}, Modelo {self.getModelo()}, Ano: {self.getAno()}, e Vagoes: {self.getnVagoes()} ")
    


