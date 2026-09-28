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
from queue import PriorityQueue

pygame.init()

WIDTH, HEIGHT = 800, 800
TILE_SIZE = 40
GRID_WIDTH = WIDTH // TILE_SIZE
GRID_HEIGHT = HEIGHT // TILE_SIZE

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (50, 50, 50)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PacMan Game")

clock = pygame.time.Clock()
FPS = 10

DIRECTIONS = {
    "UP": (0, -1),
    "DOWN": (0, 1),
    "LEFT": (-1, 0),
    "RIGHT": (1, 0)
}


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

#Labirent Oluşturma Fonksiyonu (generate_connected_maze):
def generate_connected_maze(width, height, extra_paths=0.3):
    maze = [[1 for _ in range(width)] for _ in range(height)]

    def carve_passages(x, y): #carve_passages: Rastgele bir derinlik öncelikli arama algoritması kullanılarak yollar oluşturur.
        directions = list(DIRECTIONS.values())
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx * 2, y + dy * 2
            if 0 < nx < width - 1 and 0 < ny < height - 1 and maze[ny][nx] == 1:
                maze[y + dy][x + dx] = 0
                maze[ny][nx] = 0
                carve_passages(nx, ny)

    maze[1][1] = 0
    carve_passages(1, 1)

    for y in range(1, height - 1):
        for x in range(1, width - 1):
            if maze[y][x] == 1 and random.random() < extra_paths:
                maze[y][x] = 0

    return maze


MAP = generate_connected_maze(GRID_WIDTH, GRID_HEIGHT)


class PacMan:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.score = 0
        self.lives = 5

    def move(self, dx, dy):
        new_x = (self.x + dx)
        new_y = (self.y + dy)
        if MAP[new_y][new_x] == 0:
            self.x = new_x
            self.y = new_y

    def get_position(self):
        return self.x, self.y

    def reset_position(self):
        self.x = 1
        self.y = 1


class Food:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_position(self):
        return self.x, self.y


class Ghost:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        while True:
            dx, dy = random.choice(list(DIRECTIONS.values()))
            new_x = (self.x + dx)
            new_y = (self.y + dy)
            if MAP[new_y][new_x] == 0:
                self.x = new_x
                self.y = new_y
                break

    def get_position(self):
        return self.x, self.y


class UtilityPacMan(PacMan):
    def __init__(self, x, y):
        super().__init__(x, y)

    def compute_move(self, foods, ghosts):
        min_distance = float('inf')
        best_direction = (0, 0)

        # Güvenli yiyecekleri bul
        safe_foods = [food for food in foods if all(heuristic(food.get_position(), ghost.get_position()) > 2 for ghost in ghosts)]

        # Güvenli yiyecek yoksa hareket etme
        if not safe_foods:
            return (0, 0)

        # En yakın güvenli yiyeceği hedefle
        for food in safe_foods:
            food_pos = food.get_position()
            dist = heuristic(self.get_position(), food_pos)

            # A* algoritması ile yön bul
            direction = self.get_direction_to(food_pos)
            if direction is not None and dist < min_distance:
                min_distance = dist
                best_direction = direction

        # Eğer geçerli bir yön bulunamadıysa rastgele bir yöne git
        if best_direction == (0, 0):
            for dx, dy in list(DIRECTIONS.values()):
                new_x, new_y = self.x + dx, self.y + dy
                if 0 <= new_x < GRID_WIDTH and 0 <= new_y < GRID_HEIGHT and MAP[new_y][new_x] == 0:
                    return (dx, dy)

        return best_direction

    def get_direction_to(self, target):
        start = self.get_position()
        frontier = PriorityQueue()
        frontier.put((0, start))
        came_from = {start: None}
        cost_so_far = {start: 0}

        while not frontier.empty():
            _, current = frontier.get()

            if current == target:
                break

            for dx, dy in DIRECTIONS.values():
                neighbor = (current[0] + dx, current[1] + dy)
                if 0 <= neighbor[0] < GRID_WIDTH and 0 <= neighbor[1] < GRID_HEIGHT and MAP[neighbor[1]][neighbor[0]] == 0:
                    new_cost = cost_so_far[current] + 1
                    if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                        cost_so_far[neighbor] = new_cost
                        priority = new_cost + heuristic(neighbor, target)
                        frontier.put((priority, neighbor))
                        came_from[neighbor] = current

        if target not in came_from:
            return None

        current = target
        while came_from[current] != start:
            current = came_from[current]

        direction = (current[0] - start[0], current[1] - start[1])
        return direction



class Game:
  def __init__(self, agent_controlled=False):
      self.agent_controlled = agent_controlled
      self.pacman = UtilityPacMan(1, 1) if agent_controlled else PacMan(1, 1)
      self.foods = self.generate_foods()
      self.ghosts = [Ghost(5, 5), Ghost(10, 4), Ghost(15, 5)]




  def is_accessible(self, x, y):
  # X ve Y pozisyonundaki hücreyi kontrol et
  # Eğer bu hücre bir duvara (1) sahipse, erişilemez kabul edilir
      if MAP[y][x] == 1:
              return False
  
      directions = list(DIRECTIONS.values())
      for dx, dy in directions:
          nx, ny = x + dx, y + dy
          if 0 <= nx < GRID_WIDTH and 0 <= ny < GRID_HEIGHT and MAP[ny][nx] == 0:
              return True  # Eğer çevresinde geçiş yapılabilir bir alan varsa
      return False  # Çevresinde hiç geçiş yapılabilir bir alan yoksa


  def generate_foods(self):
      foods = []
      for y, row in enumerate(MAP):
          for x, tile in enumerate(row):
              if tile == 0 and random.random() < 0.2:
                  if self.is_accessible(x, y):
                      foods.append(Food(x, y))
      return foods

  def draw_map(self):
      for y, row in enumerate(MAP):
          for x, tile in enumerate(row):
              if tile == 1:
                  pygame.draw.rect(screen, GREY, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))



  def draw_pacman(self):
      pygame.draw.circle(screen, YELLOW, (self.pacman.x * TILE_SIZE + TILE_SIZE // 2, self.pacman.y * TILE_SIZE + TILE_SIZE // 2), TILE_SIZE // 2)


  def draw_foods(self):
      for food in self.foods:
          pygame.draw.circle(screen, RED, (food.x * TILE_SIZE + TILE_SIZE // 2, food.y * TILE_SIZE + TILE_SIZE // 2), TILE_SIZE // 4)


  def draw_ghosts(self):
      for ghost in self.ghosts:
          pygame.draw.circle(screen, BLUE, (ghost.x * TILE_SIZE + TILE_SIZE // 2, ghost.y * TILE_SIZE + TILE_SIZE // 2), TILE_SIZE // 2)


  def handle_collision(self):
      pacman_position = self.pacman.get_position()
    
      foods_to_remove = [food for food in self.foods if food.get_position() == pacman_position]
      for food in foods_to_remove:
          self.foods.remove(food)
          self.pacman.score += 10
    
      for ghost in self.ghosts:
          if ghost.get_position() == pacman_position:
              self.pacman.lives -= 1
              print(f"PacMan hit a ghost! Lives remaining: {self.pacman.lives}")
              self.pacman.reset_position()
              if self.pacman.lives == 0:
                  print("Game Over! Final Score:", self.pacman.score)
                  pygame.quit()
                  exit()

  def move_ghosts(self):
      for ghost in self.ghosts:
          ghost.move()


  def run(self):
      running = True
      direction = (0, 0)
      start_ticks = pygame.time.get_ticks()  # Oyunun başlangıç zamanı


      while running:
          screen.fill(BLACK)
          self.draw_map()
          self.draw_pacman()
          self.draw_foods()
          self.draw_ghosts()


          # Geçen süreyi hesapla
          elapsed_time = (pygame.time.get_ticks() - start_ticks) // 1000  # Saniyeye çevir


          # Geçen süreyi üstte göster
          font = pygame.font.Font(None, 30) 
          time_text = font.render(f"Time: {elapsed_time}s", True, WHITE)
          screen.blit(time_text, (10, 10))  # Ekranın sol üst köşesine yaz


          # Skoru ve canları göster
          score_text = font.render(f"Score: {self.pacman.score} - Lives: {self.pacman.lives}", True, WHITE)
          screen.blit(score_text, (WIDTH - 300, 10))  # Sağ üst köşeye yaz

          for event in pygame.event.get():
              if event.type == pygame.QUIT:
                  running = False
              if event.type == pygame.KEYDOWN and not self.agent_controlled:
                  if event.key == pygame.K_UP:
                      direction = DIRECTIONS["UP"]
                  elif event.key == pygame.K_DOWN:
                      direction = DIRECTIONS["DOWN"]
                  elif event.key == pygame.K_LEFT:
                      direction = DIRECTIONS["LEFT"]
                  elif event.key == pygame.K_RIGHT:
                      direction = DIRECTIONS["RIGHT"]


          if self.agent_controlled:
              direction = self.pacman.compute_move(self.foods, self.ghosts)


          self.pacman.move(*direction)
          self.move_ghosts()
          self.handle_collision()


          # Eğer tüm yiyecekler biterse oyunu bitir
          if not self.foods:
              print("Game Over! Final Score:", self.pacman.score)
              running = False


          pygame.display.flip()
          clock.tick(FPS)


def main_menu():
  font = pygame.font.Font(None, 30)
  while True:
      screen.fill(BLACK)
      text = font.render("Press 1 for User-Controlled or 2 for AI-Controlled", True, WHITE)
      screen.blit(text, (WIDTH // 4, HEIGHT // 2 - 20))


      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              pygame.quit()
              return
          if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_1:
                  print("Starting User-Controlled Game...")
                  game_user = Game(agent_controlled=False)
                  game_user.run()
                  return
              elif event.key == pygame.K_2:
                  print("Starting AI-Controlled Game...")
                  game_ai = Game(agent_controlled=True)
                  game_ai.run()
                  return


      pygame.display.flip()
      clock.tick(FPS)


main_menu()


pygame.quit()

__PROPRIETARY_AUTH_CANARY__ = "AUTH:MUHAMMED_EMIN_KORKUNC_2021221054_AI_VERIFIED"
