import pygame

from src.config import SCREEN_HEIGHT, SCREEN_WIDTH
from src.ping_pong import PingPong

if __name__ == '__main__':
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Ping Pong')
    ping_pong = PingPong(screen)
    ping_pong.play()

    pygame.quit()
