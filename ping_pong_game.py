import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping-Pong Game")

FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
PADDLE_SPEED = 5

BALL_RADIUS = 7
BALL_SPEED_X = 5
BALL_SPEED_Y = 5

font = pygame.font.SysFont("comicsans", 40)

def draw_window(left_paddle, right_paddle, ball, left_score, right_score):
    WIN.fill(BLACK)

    pygame.draw.rect(WIN, WHITE, left_paddle)
    pygame.draw.rect(WIN, WHITE, right_paddle)

    pygame.draw.circle(WIN, WHITE, (ball.x + BALL_RADIUS, ball.y + BALL_RADIUS), BALL_RADIUS)

    left_score_text = font.render(f"{left_score}", 1, WHITE)
    right_score_text = font.render(f"{right_score}", 1, WHITE)
    WIN.blit(left_score_text, (WIDTH // 4 - left_score_text.get_width() // 2, 20))
    WIN.blit(right_score_text, (WIDTH * 3 // 4 - right_score_text.get_width() // 2, 20))

    pygame.display.update()

def main():
    clock = pygame.time.Clock()

    left_paddle = pygame.Rect(10, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = pygame.Rect(WIDTH - 10 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

    ball = pygame.Rect(WIDTH // 2 - BALL_RADIUS, HEIGHT // 2 - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)
    ball_speed_x = BALL_SPEED_X
    ball_speed_y = BALL_SPEED_Y

    left_score = 0
    right_score = 0

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and left_paddle.y > 0:
            left_paddle.y = max(0, left_paddle.y - PADDLE_SPEED)
        if keys[pygame.K_s] and left_paddle.y + PADDLE_HEIGHT < HEIGHT:
            left_paddle.y = min(HEIGHT - PADDLE_HEIGHT, left_paddle.y + PADDLE_SPEED)

        if keys[pygame.K_UP] and right_paddle.y > 0:
            right_paddle.y = max(0, right_paddle.y - PADDLE_SPEED)
        if keys[pygame.K_DOWN] and right_paddle.y + PADDLE_HEIGHT < HEIGHT:
            right_paddle.y = min(HEIGHT - PADDLE_HEIGHT, right_paddle.y + PADDLE_SPEED)

        ball.x += ball_speed_x
        ball.y += ball_speed_y

        if ball.y <= 0 or ball.y + ball.height >= HEIGHT:
            ball_speed_y *= -1

        if ball.colliderect(left_paddle) and ball_speed_x < 0:
            ball_speed_x *= -1
        if ball.colliderect(right_paddle) and ball_speed_x > 0:
            ball_speed_x *= -1

        if ball.x < 0:
            right_score += 1
            ball.center = (WIDTH // 2, HEIGHT // 2)
            ball_speed_x *= -1
        if ball.x > WIDTH:
            left_score += 1
            ball.center = (WIDTH // 2, HEIGHT // 2)
            ball_speed_x *= -1

        draw_window(left_paddle, right_paddle, ball, left_score, right_score)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()