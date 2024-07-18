from automovel import Automovel
 
class Carro(Automovel):
    def __init__(self, tipo, cor, capacidade, carroceria, motor):
      Automovel.__init__(self, tipo, cor, capacidade)
      self.carroceria = carroceria
      self.motor = motor
    def getAtributos(self):    
     print(f"Tipo: {self.tipo}\nCor: {self.cor}\nCapacidade: Até {self.capacidade} pessoas\nCarroceria: {self.carroceria}\nMotor:{self.motor}")
    def ligar(self):
        print("O carro ligou")
    def desligar(self):
        print("O carro desligou")
    def _subir_vidros(self):
        print("Os vidros estão subindo")