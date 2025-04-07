from grafo import Grafo
from busca_aestrela import AEstrela

def main():
    grafo = Grafo()
    busca = AEstrela(grafo.bucharest)
    busca.buscar(grafo.arad)

if __name__ == "__main__":
    main()
