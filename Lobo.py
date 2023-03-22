from Monstro import Monstro


class Lobo(Monstro):
    def __init__(self, pontos_de_vida, pontos_de_ataque, tipo, forca):
        super().__init__(pontos_de_vida, pontos_de_ataque, tipo)
        self.forca = forca
