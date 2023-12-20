import pygame
import sys
import random

# Initialisation de Pygame
pygame.init()

# Définition de variables
WIDTH, HEIGHT = 600, 600
LINE_COLOR = (0, 0, 0)
GRID_COLOR = (0, 0, 0)
GRID_SIZE = 3
CELL_SIZE = WIDTH // GRID_SIZE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

def draw_grid():
    for i in range(1, GRID_SIZE):
        pygame.draw.line(screen, LINE_COLOR, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), 2)
        pygame.draw.line(screen, LINE_COLOR, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), 2)

def draw_symbol(row, col, symbol):
    font = pygame.font.Font(None, 120)
    text = font.render(symbol, True, (0, 0, 0))
    text_rect = text.get_rect(center=(col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2))
    screen.blit(text, text_rect)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(GRID_SIZE):
        if all(row[col] == player for row in board):
            return True
    if all(board[i][i] == player for i in range(GRID_SIZE)):
        return True
    if all(board[i][GRID_SIZE - i - 1] == player for i in range(GRID_SIZE)):
        return True
    return False

def display_winner(player):
    font = pygame.font.Font(None, 60)
    text = font.render(f"Le joueur {player} a gagné!", True, (255, 0, 0))
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.wait(3000)

def computer_move(board, player):
    empty_cells = [(i, j) for i in range(GRID_SIZE) for j in range(GRID_SIZE) if board[i][j] == ' ']
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = player
        draw_symbol(row, col, player)

def choose_mode():
    font = pygame.font.Font(None, 40)
    text_vs_player = font.render("Press NumPad 1 for two-player mode", True, (0, 0, 0))
    text_vs_ai = font.render("Press NumPad 2 to play against AI", True, (0, 0, 0))

    while True:
        screen.fill((255, 255, 255))
        screen.blit(text_vs_player, (50, 150))
        screen.blit(text_vs_ai, (50, 200))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP1:
                    return False  # Two-player mode
                elif event.key == pygame.K_KP2:
                    return True  # AI mode

def main():
    play_against_ai = choose_mode()
    board = [[' ' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    player_turn = 'X'
    game_over = False

    while not game_over:
        screen.fill((255, 255, 255))
        draw_grid()

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

                if board[row][col] == ' ' and (not play_against_ai or player_turn == 'X'):
                    board[row][col] = player_turn
                    draw_symbol(row, col, player_turn)

                    if check_winner(board, player_turn):
                        display_winner(player_turn)
                        game_over = True
                        break

                    player_turn = 'O' if player_turn == 'X' else 'X'

        if play_against_ai and player_turn == 'O' and not game_over:
            pygame.time.wait(500) # Un petit délai pour l'IA
            computer_move(board, 'O')

            if check_winner(board, 'O'):
                display_winner('O')
                game_over = True
            else:
                player_turn = 'X'

        pygame.display.flip()

if __name__ == "__main__":
    main()
    pygame.quit()
    sys.exit()