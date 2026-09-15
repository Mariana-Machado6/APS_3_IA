from aigyminsper.search.search_algorithms import BuscaLargura, BuscaProfundidade
from aigyminsper.search.graph import State
 
 
class AgentSpecification(State):
 
    def __init__(self, op, colunas, n):
        super().__init__(op)
        self.colunas = colunas
        self.n = n
 
    def _posicao_segura(self, nova_linha, nova_coluna):
        for linha, coluna in enumerate(self.colunas):
            # mesma coluna
            if coluna == nova_coluna:
                return False
            # mesma diagonal
            if abs(linha - nova_linha) == abs(coluna - nova_coluna):
                return False
        return True
 
    def successors(self):
        successors = []
 
        proxima_linha = len(self.colunas)
        if proxima_linha >= self.n:
            return successors
 
        for coluna in range(self.n):
            if self._posicao_segura(proxima_linha, coluna):
                novas_colunas = self.colunas + [coluna]
                successors.append(
                    AgentSpecification(
                        f'rainha na linha {proxima_linha}, coluna {coluna}',
                        novas_colunas,
                        self.n
                    )
                )
 
        return successors
 
    def is_goal(self):
        return len(self.colunas) == self.n
 
    def description(self):
        return f"Problema das {self.n} rainhas"
 
    def cost(self):
        return 1
 
    def env(self):
        return str(self.colunas) + "#" + str(self.n)
 
    def to_board(self):
        tabuleiro = [[0] * self.n for _ in range(self.n)]
        for linha, coluna in enumerate(self.colunas):
            tabuleiro[linha][coluna] = 1
        return tabuleiro
 
    def print_board(self):
        for linha, coluna in enumerate(self.colunas):
            celulas = ['.'] * self.n
            celulas[coluna] = 'Q'
            print(' '.join(celulas))
 
 
def resolver(n, algoritmo='largura'):
    state = AgentSpecification('', [], n)
 
    if algoritmo == 'largura':
        algorithm = BuscaLargura()
    else:
        algorithm = BuscaProfundidade()
 
    result = algorithm.search(state, pruning="general", trace=False)
 
    print(f'\n{"=" * 30}')
    print(f'N = {n}  (busca em {algoritmo})')
    print(f'{"=" * 30}')
 
    if result is not None:
        solucao = result.state
        print('Solução encontrada!')
        print(f'Posições (linha -> coluna): {solucao.colunas}')
        print('\nTabuleiro:')
        solucao.print_board()
        print(f'\nMatriz: {solucao.to_board()}')
        print(f'Custo: {result.g}')
    else:
        print('Não achou solução')
 
 
def main():
    for n in [4, 5, 6, 7, 8]:
        resolver(n, algoritmo='largura')
 
 
if __name__ == '__main__':
    main()
 
