class Automovel():
    def __init__(self, tipo, cor, capacidade):
        self.tipo = tipo
        self.cor = cor
        self.capacidade = capacidade
    def getAtributos(self):
        print(f"Tipo: {self.tipo}\nCor: {self.cor}\nCapacidade: Até {self.capacidade} pessoas")
    def ligar(self):
        print("O automóvel está ligado")
    def desligar(self):
         print("O automóvel está desligado")
    def _limpar_parabrisa(self):
        print("O limpador de para-brisa foi ligado")
