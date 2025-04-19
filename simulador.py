from ambiente import Ambiente
from agente import AgenteSimples

def simular(rodadas=10):
    ambiente = Ambiente()
    agente = AgenteSimples()

    for i in range(rodadas):
        print(f"\n----- RODADA {i+1} -----")
        ambiente.mostrar_estado()

        percepto = ambiente.percepto()
        acao = agente.decidir_acao(percepto)

        print(f"Ação escolhida: {acao}")
        ambiente.executar_acao(acao)

        if ambiente.esta_limpo():
            print("\n>>> AMBIENTE LIMPO! Encerrando simulação.")
            break

    print("\n=== SIMULAÇÃO FINALIZADA ===")
    ambiente.mostrar_estado()

if __name__ == "__main__":
    simular()
