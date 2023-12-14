import pygame
import sys

# initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 640, 480
WHITE = (255, 255, 255)

# initialize the screen
screen = pygame.display.set_mode((
    WIDTH, HEIGHT
))
pygame.display.set_caption('Pong Game')

# paddle dimensions
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100

paddle1_x = 50
paddle1_y = (HEIGHT - PADDLE_HEIGHT) // 2

paddle2_x = WIDTH - 50 - PADDLE_WIDTH
paddle2_y = (HEIGHT - PADDLE_HEIGHT) // 2

paddle1_speed = 0
paddle2_speed = 0


BALL_SIZE = 20
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed_x = 7
ball_speed_y = 7

score_1 = 0
score_2 = 0


font = pygame.font.Font(None, 36)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                paddle1_speed = -7
            elif event.key == pygame.K_s:
                paddle1_speed = 7
            elif event.key == pygame.K_UP:
                paddle2_speed = -7
            elif event.key == pygame.K_DOWN:
                paddle2_speed = 7
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                paddle1_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                paddle2_speed = 0

    paddle1_y += paddle1_speed
    paddle2_y += paddle2_speed

    paddle1_y = max(min(paddle1_y,  HEIGHT - PADDLE_HEIGHT), 0)
    paddle2_y = max(min(paddle2_y,  HEIGHT - PADDLE_HEIGHT), 0)

    ball_x += ball_speed_x
    ball_y += ball_speed_y

    if ball_y <= 0 or ball_y >= HEIGHT - BALL_SIZE:
        ball_speed_y = -ball_speed_y


    if ((ball_x <= paddle1_x + PADDLE_WIDTH and paddle1_y <= ball_y <=  paddle1_y + PADDLE_HEIGHT) or
        (ball_x >= paddle2_x - BALL_SIZE and paddle2_y <= ball_y <= paddle2_y + PADDLE_HEIGHT)):
        ball_speed_x = -ball_speed_x


    if ball_x <= 0:
        score_2 += 1
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2
        ball_speed_x = -ball_speed_x
    elif ball_x >= WIDTH - BALL_SIZE:
        score_1 += 1
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2
        ball_speed_x = -ball_speed_x


    screen.fill((0, 0, 0))

    pygame.draw.rect(screen,WHITE,
                     (paddle1_x, paddle1_y, PADDLE_WIDTH, PADDLE_HEIGHT)
                     )

    pygame.draw.rect(screen,WHITE,
                     (paddle2_x, paddle2_y, PADDLE_WIDTH, PADDLE_HEIGHT)
                     )

    pygame.draw.ellipse(screen, WHITE,
                        (ball_x, ball_y, BALL_SIZE, BALL_SIZE))

    score_text = font.render(f'{score_1} - {score_2}', True, WHITE)
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 20))

    pygame.display.flip()

    pygame.time.Clock().tick(60)






