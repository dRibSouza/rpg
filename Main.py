from Goblin import Goblin
from Lobo import Lobo
from Personagem import Personagem
import random
import time
from tabulate import tabulate


nome = input("Informe o nome do seu personagem: ")


heroi = Personagem(20, 5, nome)
lobo = Lobo(10, 3, "fogo", 5)
goblin = Goblin(8, 2, "gelo", 5)
turno = 0

while heroi.pontos_de_vida > 0:
    print(f"TURNO {turno + 1}")
    time.sleep(1)
    print("\n\n\n")

    if turno % 2 == 0:
        print("SEU TURNO")
        time.sleep(1)
        print("\n\n\n")

        alvo = int(input(
            "Escolha seu alvo: \n 1 - para atacar o lobo \n 2 - para atacar o goblin \n Alvo: "))

        if alvo == 1:
            if lobo.pontos_de_vida <= 0:
                print(
                    "Poxa, já ouvi falar em chutar cachorro morto, agora Lobo morto é um pouco demais...")
                time.sleep(2)

            heroi.atacar(lobo)
            turno += 1
            print("Você atacou o Lobo")
            time.sleep(1)
            print("\n\n\n")
            if lobo.pontos_de_vida <= 0:
                print("Parabéns, o Lobo está morto.")
                time.sleep(1)
                print("\n\n\n")

        elif alvo == 2:
            if goblin.pontos_de_vida <= 0:
                print("É só um goblin, não um zumbi, você já pode parar de bater...")
                time.sleep(2)

            heroi.atacar(goblin)
            turno += 1
            print("Você atacou o Goblin")
            time.sleep(1)
            print("\n\n\n")

            if goblin.pontos_de_vida <= 0:
                print("Parabéns, o Goblin está morto.")
                time.sleep(1)
                print("\n\n\n")

        else:
            print("Alvo inválido, você perdeu o turno :(")
            time.sleep(1)
            turno += 1

            print("\n\n\n")

        if lobo.pontos_de_vida <= 0 and goblin.pontos_de_vida <= 0:
            print("*************** PARABÉNS, VOCÊ VENCEU ***************")
            break
    else:
        print("TURNO DOS INIMIGOS")
        time.sleep(1)
        print("\n\n\n")
        vilao = random.randint(1, 2)
        if vilao == 1:
            if lobo.pontos_de_vida > 0:
                lobo.atacar(heroi)
                print("Você foi atacado pelo Lobo")
                time.sleep(1)
                print("\n\n\n")
                turno += 1
            else:
                goblin.atacar(heroi)
                print("Você foi atacado pelo Goblin")
                time.sleep(1)
                print("\n\n\n")
                turno += 1
        else:
            if goblin.pontos_de_vida > 0:
                goblin.atacar(heroi)
                print("Você foi atacado pelo Goblin")
                time.sleep(1)
                print("\n\n\n")
                turno += 1
            else:
                lobo.atacar(heroi)
                print("Você foi atacado pelo Lobo")
                time.sleep(1)
                print("\n\n\n")
                turno += 1
    print(f"FIM DO TURNO {turno}")
    # print(f"Seu Personagem: \n{nome} \t Pontos de Vida:  {heroi.pontos_de_vida} \n Seus inimigos: \n Lobo:     {lobo.pontos_de_vida} \n Goblin:   {goblin.pontos_de_vida}")

    seresVivos = [[heroi.nome, heroi.pontos_de_vida], [
        "Lobo", lobo.pontos_de_vida], ["Goblin", goblin.pontos_de_vida]]
    print(tabulate(seresVivos, headers=[
          "Personagem", "Pontos de Vida"], tablefmt='fancy_grid'))
    time.sleep(2)
    print("\n\n\n")

if heroi.pontos_de_vida <= 0:
    print("*************** VOCÊ MORREU ***************")
