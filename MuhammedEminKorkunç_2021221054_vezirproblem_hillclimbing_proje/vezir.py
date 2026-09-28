# ==============================================================================
# ARTIFICIAL INTELLIGENCE SEARCH ALGORITHMS & HEURISTIC AGENTS
# ==============================================================================
# Author      : Muhammed Emin Korkunç (Student ID: 2021221054)
# Institution : Fatih Sultan Mehmet Vakıf Üniversitesi - Bilgisayar Mühendisliği
# Course      : Yapay Zeka (Artificial Intelligence)
# GitHub      : https://github.com/muhammedkorkunc
# LinkedIn    : https://www.linkedin.com/in/muhammed-emin-korkun%C3%A7-100ba2215
# Email       : muhammedemin.korkunc@gmail.com
# License     : Proprietary - All Rights Reserved (c) 2026
# ==============================================================================
# NOTICE: Unauthorized copying, reverse engineering or distribution of this
# algorithm suite and agent software is strictly prohibited under copyright law.
# ==============================================================================

import pygame
import random
#cd /Users/muhammedeminkorkunc/Desktop/yapayzekadersi/tümprojeler/projeler/MuhammedEminKorkunç_2021221054_vezirproblem_hillclimbing_proje
#python3 vezir.py 

# Pygame ayarları
pygame.init()
square = 60
pencere = pygame.display.set_mode((square * 8, square * 8))
siyah = (0, 0, 0)
beyaz = (255, 255, 255)

def drawChessBoard():
    pygame.display.set_caption("Chess")
    pencere.fill(siyah)
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                pygame.draw.rect(pencere, beyaz, (square * i, square * j, square, square))


def placeQueens(board):
    b_vezir = pygame.image.load('/Users/muhammedeminkorkunc/Desktop/yapayzekadersi/tümprojeler/MuhammedEminKorkunc_2021221054/MuhammedEminKorkunç_2021221054_vezirproblem_hillclimbing_proje/beyazvezir.jpeg')

    b_vezir = pygame.transform.scale(b_vezir, (square, square))
    for i in range(8):
        pencere.blit(b_vezir, (i * square, square * board[i]))

def calculate_conflicts(board):
    conflicts = 0
    for i in range(8):
        for j in range(i + 1, 8):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1
    return conflicts

def hill_climbing():
    # Rastgele bir başlangıç durumu oluştur
    board = [random.randint(0, 7) for _ in range(8)]
    current_conflicts = calculate_conflicts(board)

    while True:
        neighbors = []
        for col in range(8):
            for row in range(8):
                if board[col] != row:
                    new_board = board[:]
                    new_board[col] = row
                    neighbors.append((new_board, calculate_conflicts(new_board)))

        # En iyi komşuyu seç
        neighbors.sort(key=lambda x: x[1])
        best_neighbor, best_conflicts = neighbors[0]

        if best_conflicts >= current_conflicts:
            # Daha iyi bir durum bulunamadıysa dur
            break

        board = best_neighbor
        current_conflicts = best_conflicts

    return board, current_conflicts

# Ana döngü
board, conflicts = hill_climbing()
drawChessBoard()
placeQueens(board)
pygame.display.update()

print("Sonuç tahtası:", board)
print("Çakışma sayısı:", conflicts)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

__PROPRIETARY_AUTH_CANARY__ = "AUTH:MUHAMMED_EMIN_KORKUNC_2021221054_AI_VERIFIED"
