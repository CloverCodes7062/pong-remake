import pygame
from pygame.locals import *
import random
pygame.font.init()

WIDTH, HEIGHT = 900, 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

FPS = 60

BALL_SPEED = 5

clock = pygame.time.Clock()

pygame.display.set_caption("Pong")

sprite_group = pygame.sprite.Group()


class Base:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (self.x, self.y, self.width, self.height)

    def draw(self):
        pygame.draw.rect(WIN, self.color, (self.x, self.y, self.width, self.height))

class Player(Base):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, width, height, color)
        self.score = 0
        
    def get_rect(self):
        (self.x, self.y, self.width, self.height)

class Ball(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH / 2
        self.rect.y = HEIGHT / 2
        self.vel_x = BALL_SPEED
        self.vel_y = -BALL_SPEED
 
    def update(self, player1, player2):    
        
        if pygame.Rect.colliderect(self.rect, (player2.x, player2.y, player2.width, player2.height)):
            self.vel_x = -BALL_SPEED
        if pygame.Rect.colliderect(self.rect, (player1.x, player1.y, player1.width, player1.height)):
            self.vel_x = BALL_SPEED
        self.rect.x += self.vel_x

        if self.rect.x == WIDTH + 20:
            player1.score += 1
            reset_ball()
        if self.rect.x == 0 - 20:
            player2.score += 1
            reset_ball()
        if self.rect.y < 0:
            self.vel_y = BALL_SPEED
        if self.rect.y > HEIGHT:
            self.vel_y = -BALL_SPEED
        self.rect.y += self.vel_y

def reset_ball():
    num = random.randint(1, 2)
    if num == 1:
        num = 1
    elif num == 2:
        num = -1
    ball.rect.x = WIDTH / 2
    ball.rect.y = HEIGHT / 2
    ball.vel_x = BALL_SPEED
    ball.vel_y = -BALL_SPEED * num

ball = Ball()
sprite_group.add(ball)

def main():
    run = True
    player1_x = 20
    player1_y = 0
    player1_width = 10
    player1_height = 100
    player1_color = WHITE
    player1_vel = 5
    player1_score_font = pygame.font.SysFont("arial", 40)

    player2_x = WIDTH - 30
    player2_y = 0
    player2_width = 10
    player2_height = 100
    player2_color = WHITE
    player2_vel = 5
    player2_score_font = pygame.font.SysFont("arial", 40)

    player1 = Player(player1_x, player1_y, player1_width, player1_height, player1_color)
    player2 = Player(player2_x, player2_y, player2_width, player2_height, player2_color)

    def redraw_window():
        WIN.fill((BLACK))

        player1_score_label = player1_score_font.render(f"Score: {player1.score}", 16, (WHITE))
        player2_score_label = player2_score_font.render(f"Score: {player2.score}", 16, (WHITE))

        WIN.blit(player1_score_label, (35, 0))
        WIN.blit(player2_score_label, (WIDTH - player2_score_label.get_width() - 35, 0))
        player1.draw()
        player2.draw()
        ball.update(player1, player2)
        sprite_group.draw(WIN)

        pygame.display.update()

    while run:

        clock.tick(FPS)
        
        redraw_window()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_s] and player1.y + player1_height + player1_vel <= HEIGHT:
            player1.y += player1_vel
        if keys_pressed[pygame.K_w] and player1.y - player1_vel >= 0:
            player1.y -= player1_vel
        if keys_pressed[pygame.K_DOWN] and player2.y + player2.height + player2_vel <= HEIGHT:
            player2.y += player2_vel
        if keys_pressed[pygame.K_UP] and player2.y - player2_vel >= 0:
            player2.y -= player2_vel
        
        
def main_menu():
    title_font = pygame.font.SysFont("arial", 70)
    run = True
    while run:

        WIN.fill((0, 0, 0))
        title_label = title_font.render("Click to begin...", 16, (255, 255, 255))

        WIN.blit(title_label, ((WIDTH/2 - title_label.get_width()/2), HEIGHT/2 - title_label.get_height()))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()

main_menu()
        
