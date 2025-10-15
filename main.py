
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


    # Lista com todos os dados
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



def main():
    meu_grafo = read_graf()
    minha_matriz = t_matriz_adj(meu_grafo)
    #print(meu_grafo[2][3])

    # PERCORRE A MATRIZ DE ADJACÊNCIA (USANDO BUSCA EM PRFUNDIDADE - TEM MAIS SENTIDO)






if __name__ == "__main__":
    main()



