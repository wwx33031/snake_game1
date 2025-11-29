"""
Moduł gry Snake
Implementacja klasycznej gry Snake w pygame
"""

import pygame
import random
import sys

# Stałe gry
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
CELL_SIZE = 20
FPS = 10

# Kolory
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
DARK_GREEN = (0, 200, 0)

# Kierunki
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)


class Snake:
    """Klasa reprezentująca węża w grze"""
    
    def __init__(self, start_pos):
        """
        Inicjalizacja węża
        
        Args:
            start_pos: Tuple (x, y) - pozycja startowa głowy węża
        """
        self.body = [start_pos]
        self.direction = RIGHT
        self.grow = False
    
    def move(self):
        """Przesuwa węża w aktualnym kierunku"""
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0] * CELL_SIZE, 
                   head_y + self.direction[1] * CELL_SIZE)
        
        self.body.insert(0, new_head)
        
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False
    
    def change_direction(self, new_direction):
        """
        Zmienia kierunek węża (zabezpieczenie przed cofaniem się)
        
        Args:
            new_direction: Tuple (x, y) - nowy kierunek
        """
        # Nie pozwól na cofanie się w przeciwnym kierunku
        if (new_direction[0] * -1, new_direction[1] * -1) != self.direction:
            self.direction = new_direction
    
    def check_collision(self, width, height):
        """
        Sprawdza kolizję ze ścianami
        
        Args:
            width: Szerokość okna gry
            height: Wysokość okna gry
        
        Returns:
            True jeśli nastąpiła kolizja, False w przeciwnym razie
        """
        head_x, head_y = self.body[0]
        return (head_x < 0 or head_x >= width or 
                head_y < 0 or head_y >= height)
    
    def check_self_collision(self):
        """
        Sprawdza kolizję z własnym ciałem
        
        Returns:
            True jeśli nastąpiła kolizja, False w przeciwnym razie
        """
        return self.body[0] in self.body[1:]
    
    def eat_food(self):
        """Oznacza, że wąż zjadł jedzenie i powinien urosnąć"""
        self.grow = True
    
    def get_head(self):
        """Zwraca pozycję głowy węża"""
        return self.body[0]


class Food:
    """Klasa reprezentująca jedzenie w grze"""
    
    def __init__(self, width, height):
        """
        Inicjalizacja jedzenia
        
        Args:
            width: Szerokość okna gry
            height: Wysokość okna gry
        """
        self.width = width
        self.height = height
        self.position = self.generate_position()
    
    def generate_position(self):
        """
        Generuje losową pozycję jedzenia
        
        Returns:
            Tuple (x, y) - pozycja jedzenia
        """
        x = random.randint(0, (self.width // CELL_SIZE) - 1) * CELL_SIZE
        y = random.randint(0, (self.height // CELL_SIZE) - 1) * CELL_SIZE
        return (x, y)
    
    def respawn(self, snake_body):
        """
        Przenosi jedzenie w nowe miejsce (unika pozycji węża)
        
        Args:
            snake_body: Lista pozycji segmentów węża
        """
        while True:
            self.position = self.generate_position()
            if self.position not in snake_body:
                break
    
    def get_position(self):
        """Zwraca pozycję jedzenia"""
        return self.position


class Game:
    """Główna klasa gry zarządzająca logiką i renderowaniem"""
    
    def __init__(self):
        """Inicjalizacja gry"""
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.score = 0
        
        # Inicjalizacja węża i jedzenia
        start_x = WINDOW_WIDTH // 2
        start_y = WINDOW_HEIGHT // 2
        # Wyrównaj do siatki
        start_x = (start_x // CELL_SIZE) * CELL_SIZE
        start_y = (start_y // CELL_SIZE) * CELL_SIZE
        
        self.snake = Snake((start_x, start_y))
        self.food = Food(WINDOW_WIDTH, WINDOW_HEIGHT)
        
        # Upewnij się, że jedzenie nie pojawia się na wężu
        if self.food.position in self.snake.body:
            self.food.respawn(self.snake.body)
        
        self.running = True
        self.game_over = False
    
    def handle_events(self):
        """Obsługuje zdarzenia klawiatury i okna"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if self.game_over:
                    if event.key == pygame.K_SPACE:
                        # Restart gry
                        self.__init__()
                    elif event.key == pygame.K_ESCAPE:
                        self.running = False
                else:
                    # Sterowanie wężem
                    if event.key == pygame.K_UP:
                        self.snake.change_direction(UP)
                    elif event.key == pygame.K_DOWN:
                        self.snake.change_direction(DOWN)
                    elif event.key == pygame.K_LEFT:
                        self.snake.change_direction(LEFT)
                    elif event.key == pygame.K_RIGHT:
                        self.snake.change_direction(RIGHT)
                    elif event.key == pygame.K_ESCAPE:
                        self.running = False
    
    def update(self):
        """Aktualizuje stan gry"""
        if not self.game_over:
            self.snake.move()
            
            # Sprawdź kolizje
            if self.snake.check_collision(WINDOW_WIDTH, WINDOW_HEIGHT):
                self.game_over = True
            elif self.snake.check_self_collision():
                self.game_over = True
            
            # Sprawdź czy wąż zjadł jedzenie
            if self.snake.get_head() == self.food.get_position():
                self.snake.eat_food()
                self.score += 10
                self.food.respawn(self.snake.body)
    
    def draw(self):
        """Renderuje grę na ekranie"""
        self.screen.fill(BLACK)
        
        if not self.game_over:
            # Rysuj węża
            for i, segment in enumerate(self.snake.body):
                if i == 0:
                    # Głowa węża - ciemniejszy zielony
                    pygame.draw.rect(self.screen, DARK_GREEN, 
                                   (segment[0], segment[1], CELL_SIZE, CELL_SIZE))
                else:
                    # Ciało węża - jasny zielony
                    pygame.draw.rect(self.screen, GREEN, 
                                   (segment[0], segment[1], CELL_SIZE, CELL_SIZE))
            
            # Rysuj jedzenie
            food_pos = self.food.get_position()
            pygame.draw.rect(self.screen, RED, 
                           (food_pos[0], food_pos[1], CELL_SIZE, CELL_SIZE))
            
            # Wyświetl wynik
            score_text = self.font.render(f"Wynik: {self.score}", True, WHITE)
            self.screen.blit(score_text, (10, 10))
        else:
            # Ekran końca gry
            game_over_text = self.font.render("GAME OVER", True, WHITE)
            score_text = self.font.render(f"Twój wynik: {self.score}", True, WHITE)
            restart_text = pygame.font.Font(None, 24).render(
                "Naciśnij SPACE aby zagrać ponownie lub ESC aby wyjść", True, WHITE)
            
            # Wyśrodkuj teksty
            game_over_rect = game_over_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 60))
            score_rect = score_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 20))
            restart_rect = restart_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 20))
            
            self.screen.blit(game_over_text, game_over_rect)
            self.screen.blit(score_text, score_rect)
            self.screen.blit(restart_text, restart_rect)
        
        pygame.display.flip()
    
    def run(self):
        """Główna pętla gry"""
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        
        pygame.quit()
        return self.score


def start_game():
    """
    Funkcja uruchamiająca grę
    
    Returns:
        int - wynik uzyskany w grze
    """
    game = Game()
    score = game.run()
    return score

