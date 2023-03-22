from SerVivo import SerVivo


class Monstro(SerVivo):
    def __init__(self, pontos_de_vida, pontos_de_ataque, tipo):
        super().__init__(pontos_de_vida, pontos_de_ataque)
        self.tipo = tipo
