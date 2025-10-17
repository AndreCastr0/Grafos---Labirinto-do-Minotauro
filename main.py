import heapq
import random



#LETURA DE UM ARQUIVO E PREENCHIMENTO DA ESTRUTURA GRAFO
def read_graf():
    with open('grafo.txt', 'r', encoding='utf-8') as arquivo:  # coloca conteudo do txt em arquivo
        conteudo = arquivo.read()  # guarda o texto
        vet_linhas = conteudo.splitlines()  # divide arquivo em strings baseadas na quebra de linha
        q_linhas = len(vet_linhas)  # conta a quantidade de linhas
        cont_list = 0
        list_arestas = []

        for i in range(q_linhas):
            if i == 0:
                q_vertices = int(vet_linhas[0])  # linha

            if i == 1:
                n_arestas = int(vet_linhas[1])

            if i > 1 and i <= q_linhas - 6:  # se for uma aresta
                partes = vet_linhas[i].split()
                list_arestas.append(tuple(map(int, partes)))
                cont_list += 1

            if i == q_linhas - 5:
                vert_in = int(vet_linhas[i])

            if i == q_linhas - 4:
                vert_out = int(vet_linhas[i])

            if i == q_linhas - 3:
                minot_ini_pos = int(vet_linhas[i])

            if i == q_linhas - 2:
                perc_minot_val = int(vet_linhas[i])

            if i == q_linhas - 1:
                max_temp = int(vet_linhas[i])


    # Estrutura que possui todos os dados do campo(grafo)
    dados_grafo = [
        q_vertices,
        n_arestas,
        list_arestas,
        vert_in,
        vert_out,
        minot_ini_pos,
        perc_minot_val,
        max_temp
    ]

    """
    # Impressões de verificação
    print(conteudo)
    print(vet_linhas)
    print(q_linhas)
    print(q_vertices)
    print(n_arestas)
    print(list_arestas)
    print(vert_in)
    print(vert_out)
    print(minot_ini_pos)
    print(perc_minot_val)
    print(max_temp)

    """

    return dados_grafo


#TRANSFORMA EM UMA MATRIZ DE ADJACÊNCIA
def t_matriz_adj(meu_grafo):
    q_vertices = meu_grafo[0]
    matriz_adj = [[0]*q_vertices for _ in range(q_vertices)] #cria uma matriz preenchida com zeros

    for i in range(len(meu_grafo[2])): #percorrer a lista de arestas preencher a matriz com a existencia de arestas
        aresta = meu_grafo[2][i]
        u = aresta[0]
        v = aresta[1]
        peso = aresta[2]

        ui = u - 1 #os vértices são encontrados na posição anterior a eles na matriz
        vi = v - 1

        matriz_adj[ui][vi] = peso

    return matriz_adj



#PERSONAGENS
class minotauro:
    def __init__(self, posicao_inicial, grafo, parametro_percepcao): #permitir ter minotauros com valores diferentes
        self._alive = True
        self._pos = posicao_inicial
        self._vel = 1
        self._detect = False
        self._percepcao = parametro_percepcao
        self.grafo = grafo
        # Removidas as variáveis da DFS

    # ALIVE
    def set_die(self): #mata o minotauro
            self._alive = False

    def get_alive(self): # olha se está morto
        return self._alive

    #POSIÇÃO
    def set_pos(self, posicao):
        self._pos = posicao

    def get_pos(self):
        return self._pos

    # DETECT
    def get_cheiro(self): #verifica se está sentindo cheiro
        return self._detect

    def set_cheiro_true(self): #faz sentir o cheiro
        if self._detect == False:
            self._detect = True
            self._vel = 2

    def set_cheiro_false(self): #faz esquecer o cheiro
        if self._detect == True:
            self._detect = False
            self._vel = 1

    def get_mino_vel(self):
        return self._vel

    def set_percepcao(self, v_percep): #seta a percepção do minotauro
        self._percepcao = v_percep

    def get_percepcao(self): #indicado de percepção em relação ao entrante
        return self._percepcao






    # DETECÇÃO DO PRISIONEIRO
    def detectar_prisioneiro(self, posicao_prisioneiro): #partindo do minotauro, verifique se encontra o entrante e compara com a percepcao
        distancias, _ = self.dijkstra(self._pos)
        return distancias[posicao_prisioneiro] <= self._percepcao


    # MOVIMENTAÇÃO DE PERSEGUIÇÃO PADRÃO PARA ESTADO DE PERSEGUIÇÃO
    def dijkstra(self, origem): #
        n = len(self.grafo)
        dist = [float('inf')] * n #atribui infinito para as distâncias não
        pred = [-1] * n #iniciando o vetor com -1
        dist[origem] = 0 #distancia da origem para origem é zero
        heap = [(0, origem)]  #heap com tupla distância,vértice)

        while heap:
            distancia_atual, u = heapq.heappop(heap) #extrai o vértice com menor distância estimada

            if distancia_atual > dist[u]:
                continue

            for v in range(n):
                if self.grafo[u][v] != float('inf'):
                    peso_aresta = self.grafo[u][v]
                    nova_distancia = distancia_atual + peso_aresta

                    if nova_distancia < dist[v]:
                        dist[v] = nova_distancia
                        pred[v] = u
                        heapq.heappush(heap, (nova_distancia, v))

        return dist, pred

    def reconstruir_caminho(self, pred, destino):
        caminho = []
        atual = destino
        while atual != -1:
            caminho.append(atual)
            atual = pred[atual]
        caminho.reverse()
        return caminho

    #MOVIMENTAÇÃO DO MINOTAURO ENQUANTO NÃO DETECTAR O ENTRANTE
    def mover_aleatorio(self):
        vizinhos = []
        for v in range(len(self.grafo)):
            if self.grafo[self._pos][v] != float('inf') and v != self._pos:
                vizinhos.append(v)

        if vizinhos:
            proximo = random.choice(vizinhos)
            self._pos = proximo
            return proximo
        return self._pos


    # MOVIMENTAÇÃO DE PERSEGUIÇÃO PADRÃO
    def mover_perseguicao(self, posicao_prisioneiro):
        # Primeiro movimento
        dist, pred = self.dijkstra(self._pos)
        caminho = self.reconstruir_caminho(pred, posicao_prisioneiro)

        if len(caminho) > 1:
            self._pos = caminho[1]

        # Segundo movimento (se ainda não alcançou)
        if self._pos != posicao_prisioneiro:
            dist, pred = self.dijkstra(self._pos)
            caminho = self.reconstruir_caminho(pred, posicao_prisioneiro)

            if len(caminho) > 1:
                self._pos = caminho[1]

    #MÉTODO PRINCIPAL DE MOVIMENTO
    def mover(self, posicao_prisioneiro):
        if not self._alive:  # Minotauro morto não se move
            return self._pos

        if self.detectar_prisioneiro(posicao_prisioneiro):
            if not self._detect:
                self.set_cheiro_true()
            self.mover_perseguicao(posicao_prisioneiro)
        else:
            if self._detect:
                self.set_cheiro_false()
            self.mover_aleatorio()  # Agora chama o movimento aleatório
        return self._pos







class entrante:
    def __init__(self, posicao_inicial, grafo_real, tempo_maximo):
        self._alive = True
        self._pos = posicao_inicial
        self._save = False
        self._food = tempo_maximo  # Comida inicial = tempo máximo
        self.grafo_real = grafo_real

        # Para controle da DFS - exploração sistemática
        self.visitados = set([self._pos])
        self.pilha = [self._pos]  # Pilha para backtracking (novelo de lã)

    # ESTADO BÁSICO
    def set_die(self):
        self._alive = False

    def get_alive(self):
        return self._alive

    def set_save(self):
        self._save = True

    def get_save(self):
        return self._save

    def set_food(self, food):
        self._food = food

    def get_food(self):
        return self._food

    def set_pos(self, posicao):
        self._pos = posicao

    def get_pos(self):
        return self._pos

    # ESTRATÉGIA DE EXPLORAÇÃO SIMPLES
    def explorar_dfs(self):
        atual = self._pos

        # Procura por vizinhos não visitados
        vizinhos_nao_visitados = []
        for vizinho in range(len(self.grafo_real)):
            if (self.grafo_real[atual][vizinho] != float('inf') and
                    vizinho != atual and
                    vizinho not in self.visitados):
                vizinhos_nao_visitados.append(vizinho)

        if vizinhos_nao_visitados:
            # Escolhe o primeiro vizinho não visitado
            proximo = vizinhos_nao_visitados[0]
            self.visitados.add(proximo)
            self.pilha.append(atual)  # Guarda posição atual para backtrack
            self._pos = proximo
            return proximo
        else:
            #voltar pelo novelo de lã
            if self.pilha:
                backtrack_pos = self.pilha.pop()
                self._pos = backtrack_pos
                return backtrack_pos

        return atual  # Não se move se não há opções


    def mover(self):
        if self._save:
            return self._pos  # Já escapou, não se move
        if not self._alive:
            return self._pos  # Está morto, não se move

        #  CONTROLE DE COMIDA
        self._food -= 1  # Gasta 1 unidade de comida por movimento
        if self._food <= 0:
            self._alive = False  # Morreu de fome
            return self._pos

        # Modo exploração
        return self.explorar_dfs()


    # MÉTODO PARA VERIFICAR SE ENCONTROU A SAÍDA
    def verificar_saida(self, saida):
        if self._pos == saida:
            self.set_save()
            return True
        return False

    def get_vertices_visitados(self):
        return self.visitados

    def get_food_remaining(self):
        return self._food



def verificar_e_resolver_batalha(entr, mino):

    if not entr.get_alive() or not mino.get_alive():
        return False  # Ambos precisam estar vivos para batalhar

    if entr.get_pos() == mino.get_pos():
        print("BATALHA ENTRE MINOTAURO E ENTRANTE!")

        # 1% de chance do entrante vencer
        if random.random() <= 0.01:
            print("ENTRANTE VENCEU O MINOTAURO!")
            mino.set_die()  # Minotauro morre
            # Entrante continua vivo e pode continuar
        else:
            print("MINOTAURO DEVOROU O ENTRANTE!")
            entr.set_die()  # Entrante morre

        return True

    return False





if __name__ == "__main__":
    main()



