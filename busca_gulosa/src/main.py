from grafo import Grafo
from busca_gulosa import BuscaGulosa

def main():
    grafo = Grafo()
    busca = BuscaGulosa(grafo.bucharest)

    print(">>> Executando Busca Gulosa de Arad até Bucharest <<<\n")
    busca.buscar(grafo.arad)

if __name__ == "__main__":
    main()