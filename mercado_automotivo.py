from automovel import Automovel
 
class MercadoAutomotivo(Automovel):
     def __init__(self, tipo, cor, capacidade, demanda, modelo):
      Automovel.__init__(self, tipo, cor, capacidade)
      self.demanda = demanda
      self.modelo = modelo
     def getAtributos(self):
         print(f"Tipo: {self.tipo}\nCor: {self.cor}\nCapacidade: Até {self.capacidade} pessoas\nDemanda:{self.demanda}\nModelo:{self.modelo}")
     def ligar(self):
        print("O automóvel ligou")
     def desligar(self):
        print("O automóvel desligou")
     def _informarDemanda(self):
        print(f"A demanda é {self.demanda}")
