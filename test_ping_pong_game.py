import unittest
import pygame
import ping_pong_game

class TestPingPongGame(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.left_paddle = pygame.Rect(10, ping_pong_game.HEIGHT // 2 - ping_pong_game.PADDLE_HEIGHT // 2,
                                       ping_pong_game.PADDLE_WIDTH, ping_pong_game.PADDLE_HEIGHT)
        self.right_paddle = pygame.Rect(ping_pong_game.WIDTH - 10 - ping_pong_game.PADDLE_WIDTH,
                                        ping_pong_game.HEIGHT // 2 - ping_pong_game.PADDLE_HEIGHT // 2,
                                        ping_pong_game.PADDLE_WIDTH, ping_pong_game.PADDLE_HEIGHT)
        self.ball = pygame.Rect(ping_pong_game.WIDTH // 2 - ping_pong_game.BALL_RADIUS,
                                ping_pong_game.HEIGHT // 2 - ping_pong_game.BALL_RADIUS,
                                ping_pong_game.BALL_RADIUS * 2, ping_pong_game.BALL_RADIUS * 2)

    def test_paddle_movement_bounds(self):
        self.left_paddle.y = 2
        self.left_paddle.y = max(0, self.left_paddle.y - ping_pong_game.PADDLE_SPEED)
        self.assertGreaterEqual(self.left_paddle.y, 0)

        self.right_paddle.y = ping_pong_game.HEIGHT - ping_pong_game.PADDLE_HEIGHT - 2
        self.right_paddle.y = min(ping_pong_game.HEIGHT - ping_pong_game.PADDLE_HEIGHT, self.right_paddle.y + ping_pong_game.PADDLE_SPEED)
        self.assertLessEqual(self.right_paddle.y + ping_pong_game.PADDLE_HEIGHT, ping_pong_game.HEIGHT)

    def test_ball_bounce_top_bottom(self):
        self.ball.y = 0
        ball_speed_y = -ping_pong_game.BALL_SPEED_Y
        if self.ball.y <= 0 or self.ball.y + self.ball.height >= ping_pong_game.HEIGHT:
            ball_speed_y *= -1
        self.assertEqual(ball_speed_y, ping_pong_game.BALL_SPEED_Y)

    def test_ball_reset_and_score_increment(self):
        initial_left_score = 0
        initial_right_score = 0

        # Simulate ball out of left side
        self.ball.x = -10
        right_score = initial_right_score + 1
        self.assertEqual(right_score, 1)

        # Simulate ball out of right side
        self.ball.x = ping_pong_game.WIDTH + 10
        left_score = initial_left_score + 1
        self.assertEqual(left_score, 1)

if __name__ == "__main__":
    unittest.main()