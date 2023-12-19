import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Définition de variables
WIDTH, HEIGHT = 500, 500
LINE_COLOR = (0, 0, 0)
GRID_COLOR = (0, 0, 0)
GRID_SIZE = 3
CELL_SIZE = WIDTH // GRID_SIZE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic tac Toe")

def draw_grid():
    for i in range(1, GRID_SIZE):
        # lignes verticales
        pygame.draw.line(screen, LINE_COLOR, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), 2)
        # lignes horizontales
        pygame.draw.line(screen, LINE_COLOR, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), 2)

# Fonction pour dessiner le symbole (X ou O)
def draw_symbol(row, col, symbol):
    font = pygame.font.Font(None, 120)
    text = font.render(symbol, True, (0, 0, 0))
    text_rect = text.get_rect(center=(col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2))
    screen.blit(text, text_rect)

# Fonction pour vérifier le vainqueur
def check_winner(board, player):
    # Vérifie les lignes
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Vérifie les colonnes
    for col in range(GRID_SIZE):
        if all(row[col] == player for row in board):
            return True
    # Vérifie les diagonales
    if all(board[i][i] == player for i in range(GRID_SIZE)):
        return True
    if all(board[i][GRID_SIZE - i - 1] == player for i in range(GRID_SIZE)):
        return True
    return False

# Fonction pour afficher le gagnant (joueur x ou o)
def display_winner(player):
    font = pygame.font.Font(None, 60)
    text = font.render(f"Le joueur {player} a gagné!", True, (255, 0, 0))
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.wait(3000)  # Attendre 3 secondes avant de quitter le jeu

# Fonction principale du jeu
def main():
    board = [[' ' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    player_turn = 'X'
    game_over = False

    while not game_over:
        # Efface l'écran
        screen.fill((255, 255, 255))
        
        # Dessine la grille
        draw_grid()

        # Dessine les symboles déjà joués
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if board[i][j] != ' ':
                    draw_symbol(i, j, board[i][j])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                x, y = event.pos
                col = x // CELL_SIZE
                row = y // CELL_SIZE

                if board[row][col] == ' ':
                    board[row][col] = player_turn
                    draw_symbol(row, col, player_turn)

                    # Vérifie si le joueur actuel a gagné (le gagnant)
                    if check_winner(board, player_turn):
                        display_winner(player_turn)
                        game_over = True

                    if player_turn == 'X':
                        player_turn = 'O'
                    else:
                        player_turn = 'X'

        # Met à jour l'affichage
        pygame.display.flip()

if __name__ == "__main__":
    main()
    pygame.quit()
    sys.exit()
