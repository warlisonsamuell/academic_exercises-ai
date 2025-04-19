class Ambiente:
    def __init__(self):
        self.locais = ['A', 'B']
        self.estado = {'A': 'sujo', 'B': 'sujo'}
        self.posicao_agente = 'A'
        self.pontuacao = 0

    def percepto(self):
        return self.posicao_agente, self.estado[self.posicao_agente]

    def executar_acao(self, acao):
        if acao == 'aspirar':
            if self.estado[self.posicao_agente] == 'sujo':
                self.estado[self.posicao_agente] = 'limpo'
                self.pontuacao += 10
        elif acao == 'direita':
            if self.posicao_agente == 'A':
                self.posicao_agente = 'B'
                self.pontuacao -= 1
        elif acao == 'esquerda':
            if self.posicao_agente == 'B':
                self.posicao_agente = 'A'
                self.pontuacao -= 1

    def mostrar_estado(self):
        print(f"Posição do agente: {self.posicao_agente}")
        print(f"Estado dos locais: {self.estado}")
        print(f"Pontuação: {self.pontuacao}")

    def esta_limpo(self):
        return all(val == 'limpo' for val in self.estado.values())
