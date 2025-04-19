class AgenteSimples:
    def decidir_acao(self, percepto):
        local, situacao = percepto

        if situacao == 'sujo':
            return 'aspirar'
        elif local == 'A':
            return 'direita'
        else:
            return 'esquerda'
