import random

import pygame

from src.config import *

pygame.init()

class PingPong:
    def __init__(self, screen):
        self.screen = screen
        self.paddle1 = pygame.Rect(PADDLE1_X, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.paddle2 = pygame.Rect(PADDLE2_X, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.ball = pygame.Rect(ball_x, ball_y, BALL_WIDTH, BALL_HEIGHT)
        self.primary_font = pygame.font.Font(None, 36)
        self.running = True
        self.dark_mode = None
        self.ball_speed = 5
        self.score1 = 0
        self.score2 = 0
        self.ball_dx = self.ball_speed * random.choice([-1, 1])
        self.ball_dy = self.ball_speed * random.choice([-1, 1])
        self.exit_time = self.set_mode()

    def draw_objects(self):
        pygame.draw.rect(self.screen, RED, self.paddle1)
        pygame.draw.rect(self.screen, RED, self.paddle2)
        pygame.draw.ellipse(self.screen, BLUE, self.ball)

    def move_paddle(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.paddle1.top -= PADDLE_SPEED
        elif keys[pygame.K_DOWN]:
            self.paddle1.bottom += PADDLE_SPEED

        if keys[pygame.K_w]:
            self.paddle2.top -= PADDLE_SPEED
        elif keys[pygame.K_s]:
            self.paddle2.bottom += PADDLE_SPEED

        if self.paddle1.top <= 0:
            self.paddle1.top = 0
        elif self.paddle1.bottom >= SCREEN_HEIGHT:
            self.paddle1.bottom = SCREEN_HEIGHT

        if self.paddle2.top <= 0:
            self.paddle2.top = 0
        elif self.paddle2.bottom >= SCREEN_HEIGHT:
            self.paddle2.bottom = SCREEN_HEIGHT

    def check_collision(self, paddle, ball):
        if ball.colliderect(paddle):
            return True
        return False

    def reset_ball_position(self):
        # Randomly select the ball position after each round
        side = random.choice(['Left', 'Right'])
        if side == 'Left':
            self.ball.x = PADDLE2_X + PADDLE_WIDTH + 10
            self.ball_dx = self.ball_speed
        elif side == 'Right':
            self.ball.x = SCREEN_WIDTH - (10 + PADDLE_WIDTH + 10 + BALL_WIDTH)
            self.ball_dx = -self.ball_speed
        self.ball.y = (SCREEN_HEIGHT // 2) - (BALL_HEIGHT // 2)
        return self.ball_dx

    def reset_paddle_position(self):
        self.paddle1.y = (SCREEN_HEIGHT // 2) - (PADDLE_HEIGHT // 2)
        self.paddle2.y = (SCREEN_HEIGHT // 2) - (PADDLE_HEIGHT // 2)

    def show_scores(self):
        first_score = self.primary_font.render(f'{player1_name}: {self.score1}', True, GREEN)
        second_score = self.primary_font.render(f'{player2_name}: {self.score2}', True, GREEN)
        self.screen.blit(first_score, (10, 10))
        self.screen.blit(second_score, (SCREEN_WIDTH - (second_score.get_width() + 10), 10))

    def show_game_over_message(self):
        game_over_font = pygame.font.Font(None, 52)
        message = game_over_font.render('Game Over', True, RED)
        show_score1 = self.primary_font.render(f'Player {player1_name}: {self.score1}', True, BLUE)
        show_score2 = self.primary_font.render(f'Player {player2_name}: {self.score2}', True, BLUE)
        self.screen.blit(
            message,
            (SCREEN_WIDTH // 2 - message.get_width() // 2, SCREEN_HEIGHT // 2 - message.get_height() // 2 - 30)
        )
        self.screen.blit(
            show_score1,
            (SCREEN_WIDTH // 2 - show_score1.get_width() // 2, SCREEN_HEIGHT // 2 + message.get_height())
        )
        self.screen.blit(
            show_score2,
            (SCREEN_WIDTH // 2 - show_score2.get_width() // 2, SCREEN_HEIGHT // 2 + message.get_height() + 50)
        )

    def set_mode(self):
        exit_set_mode_function_time = None
        inner_running = True
        while inner_running:
            self.screen.fill('grey')
            mode_message = self.primary_font.render('Press L for Light mode and D for Dark mode.', True, BLUE)
            self.screen.blit(
                mode_message,
                (SCREEN_WIDTH // 2 - mode_message.get_width() // 2, SCREEN_HEIGHT // 2 - mode_message.get_height() // 2)
            )
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    inner_running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_l:
                        self.dark_mode = False
                        inner_running = False
                    elif event.key == pygame.K_d:
                        self.dark_mode = True
                        inner_running = False
        if exit_set_mode_function_time is None:
            exit_set_mode_function_time = pygame.time.get_ticks()
        return exit_set_mode_function_time

    def play(self):
        ball_speed_increase = 0.15
        target_round = 3
        ball_in_motion = True
        game_over_call_time = None
        clock = pygame.time.Clock()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        ball_in_motion = True

            current_time = pygame.time.get_ticks()
            self.move_paddle()

            if self.check_collision(self.paddle2, self.ball):
                self.ball_dx = self.ball_speed
                self.ball_speed += ball_speed_increase
            elif self.check_collision(self.paddle1, self.ball):
                self.ball_dx = -self.ball_speed
                self.ball_speed += ball_speed_increase

            if ball_in_motion:
                if current_time - self.exit_time >= initial_start_delay:
                    self.ball.x += self.ball_dx
                    self.ball.y += self.ball_dy

            if self.ball.left <= 0:
                self.score2 += 1
            elif self.ball.right >= SCREEN_WIDTH:
                self.score1 += 1

            if self.ball.top <= 0 or self.ball.bottom >= SCREEN_HEIGHT:
                self.ball_dy *= -1
            elif self.ball.left <= 0 or self.ball.right >= SCREEN_WIDTH:
                ball_in_motion = False
                self.ball_speed = 5  # Set ball speed to initial value
                self.reset_paddle_position()
                self.ball_dx = self.reset_ball_position()

            if self.dark_mode:
                self.screen.fill('#212121')
            else:
                self.screen.fill('#F5F5F5')

            if self.score1 == target_round or self.score2 == target_round:
                self.show_game_over_message()
                if game_over_call_time is None:
                    game_over_call_time = pygame.time.get_ticks()
                # Create a 3-second delay before exiting the program
                elif pygame.time.get_ticks() - game_over_call_time >= 3000:
                    self.running = False
            else:
                self.draw_objects()
                self.show_scores()

            pygame.display.update()
            clock.tick(60)


if __name__ == '__main__':
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Ping Pong')
    ping_pong = PingPong(screen)
    ping_pong.play()

    pygame.quit()
