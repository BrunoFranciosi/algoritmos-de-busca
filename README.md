# Algoritmos de Busca 

- Busca Gulosa
- A* (A Estrela)

A ideia é demonstrar o funcionamento desses algoritmos usando como exemplo o famoso problema do **Mapa da Romênia**, cujo objetivo é encontrar o caminho mais eficiente entre duas cidades.

---
## 📌 Mapa de Exemplo

<div align="center">
  <img src="imagens/mapa_romenia.png" alt="Mapa da Romênia" width="500"/>
</div>

O objetivo dos algoritmos é encontrar o caminho entre a cidade de **Arad** até **Bucharest**, levando em conta a distância estimada até o objetivo (heurística).

---

## 🔍 Algoritmo de Busca Gulosa

A **Busca Gulosa** seleciona o próximo nó a ser explorado com base em uma estimativa de quão próximo ele está de um objetivo.

Ela **não garante o caminho mais curto**, mas é rápida e simples de implementar.

### Como funciona?

1. Começa no nó inicial (ex: Arad).
2. Ordena os nós adjacentes com base na distância até o objetivo.
3. Visita o nó com menor distância estimada.
4. Repete até chegar no destino.

---

## Estrutura do código

Os arquivos principais estão na pasta `src/`:

- `grafo.py`: definição dos vértices e conexões do mapa.
- `vetor_ordenado.py`: estrutura auxiliar para ordenar os vértices por heurística.
- `busca_gulosa.py`: implementação do algoritmo.
- `main.py`: script principal para executar o algoritmo.


---
--- 

## 🔍 Algoritmo A* (A Estrela)

O A* é um algoritmo de busca heurística que combina o custo do caminho já percorrido com uma estimativa do custo restante até o destino.
-> utiliza função heurística para estimar a distância do nó atual até o nó objetivo, o que ajuda a **guiar** a busca na direção certa.

Ela é ótima, é eficiente, porém não é completo, para grafos grandes e complexos se torna caro.

$f(n) = g(n) + h(n)$

$g(n)$: custo real do caminho do início até o nó n

$h(n)$: estimativa (heurística) do custo até o objetivo

$f(n)$: custo total estimado para chegar ao objetivo passando por n

---

## Estrutura do código

Os arquivos principais estão na pasta `src/`:

- `grafo.py`: definição dos vértices e conexões do mapa.
- `vetor_ordenado.py`: estrutura auxiliar para ordenar os vértices por heurística.
- `busca_gulosa.py`: implementação do algoritmo.
- `main.py`: script principal para executar o algoritmo.

