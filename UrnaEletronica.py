class UrnaEletronica:
    def __init__(self):
        self.candidatos = [{"nome_candidato": "Danilo", "partido": "Qualquer um"}, {
            "nome_candidato": "Bruna", "partido": "Outro"}]

    def exibe_candidatos(self):
        for candidato in self.candidatos:
            print("Nome: ", candidato.get("nome_candidato"))
            print("Partido: ", candidato.get("partido"))

    def adicionar_candidato(self, nome_candidato, partido):
        self.candidatos.append(
            {"nome_candidato": nome_candidato, "partido": partido})

    def remove_ultimo_candidato(self):
        self.candidatos.pop()

    def atualizar_candidato(self, indice, chave, valor):
        # notação para acessar uma lista de dicionarios utilizando o indice chave e valor
        self.candidatos[indice][chave] = valor


print("#############MOSTRA OS CANDIDATOS###################")
urna = UrnaEletronica()

urna.exibe_candidatos()


print("##############ADICIONA CANDIDATO##################")

urna.adicionar_candidato("Vagner", "OUTRO")

urna.exibe_candidatos()

print("#############REMOVE ULTIMO CANDIDATO###################")

urna.remove_ultimo_candidato()

urna.exibe_candidatos()

print("##############ATUALIZA UM CANDIDATO##################")

urna.atualizar_candidato(0, "nome_candidato", "AQUI")

urna.exibe_candidatos()
