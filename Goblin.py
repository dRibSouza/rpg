from Monstro import Monstro


class Goblin(Monstro):
    def __init__(self, pontos_de_vida, pontos_de_ataque, tipo, inteligencia):
        super().__init__(pontos_de_vida, pontos_de_ataque, tipo)
        self.inteligencia = inteligencia
