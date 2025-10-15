
"""
import pygame
import sys
import math
#import personagens





# Inicializar Pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Visualizador de Grafo")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
GRAY = (200, 200, 200)

# Fonte
font = pygame.font.Font(None, 24)


def criar_grafo():
    # Entrada do usuário
    print("=== CONFIGURAÇÃO DO GRAFO ===")

    n_vertices = 5  # int(input("Número de vértices: "))
    n_arestas = 4  # int(input("Número de arestas: "))

    print("\nDigite as conexões (formato: origem destino):")
    arestas = [(0, 1),(3,2), (1, 2), (2, 3), (3, 4)]
    # for i in range(n_arestas):
    # conexao = input(f"Aresta {i+1}: ").split()
    # origem, destino = int(conexao[0]), int(conexao[1])
    # arestas.append((origem, destino))

    vertice_jogador1 = 1  # int(input("\nVértice do Jogador 1: "))
    vertice_jogador2 = 3  # int(input("Vértice do Jogador 2: "))

    return n_vertices, arestas, vertice_jogador1, vertice_jogador2


def calcular_posicoes(n_vertices):
    # Distribuir vértices em um círculo
    posicoes = []
    centro_x, centro_y = WIDTH // 2, HEIGHT // 2
    raio = min(WIDTH, HEIGHT) // 3

    for i in range(n_vertices):
        angulo = 2 * math.pi * i / n_vertices
        x = centro_x + raio * math.cos(angulo)
        y = centro_y + raio * math.sin(angulo)
        posicoes.append((x, y))

    return posicoes


def desenhar_grafo(n_vertices, arestas, posicoes, vertice_jogador1, vertice_jogador2):
    screen.fill(WHITE)

    # Desenhar arestas
    for origem, destino in arestas:
        if origem < n_vertices and destino < n_vertices:
            pygame.draw.line(screen, GRAY, posicoes[origem], posicoes[destino], 2)

    # Desenhar vértices
    for i, (x, y) in enumerate(posicoes):
        # Verificar qual jogador está no vértice
        if i == vertice_jogador1:
            cor = RED
        elif i == vertice_jogador2:
            cor = BLUE
        else:
            cor = GREEN

        pygame.draw.circle(screen, cor, (int(x), int(y)), 20)

        # Número do vértice
        texto = font.render(str(i), True, BLACK)
        screen.blit(texto, (int(x) - 8, int(y) - 8))

    # Legenda
    pygame.draw.circle(screen, RED, (50, 30), 10)
    texto_j1 = font.render("Jogador 1", True, BLACK)
    screen.blit(texto_j1, (65, 22))

    pygame.draw.circle(screen, BLUE, (200, 30), 10)
    texto_j2 = font.render("Jogador 2", True, BLACK)
    screen.blit(texto_j2, (215, 22))

    pygame.draw.circle(screen, GREEN, (350, 30), 10)
    texto_vazio = font.render("Vértice Vazio", True, BLACK)
    screen.blit(texto_vazio, (365, 22))

    pygame.display.flip()


def main():
    # Obter dados do grafo
    n_vertices, arestas, vertice_jogador1, vertice_jogador2 = criar_grafo()

    # Calcular posições dos vértices
    posicoes = calcular_posicoes(n_vertices)

    # Loop principal
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # Desenhar o grafo
        desenhar_grafo(n_vertices, arestas, posicoes, vertice_jogador1, vertice_jogador2)

    pygame.quit()
    sys.exit()


"""
