import pygame, sys
from functions import(
    main_menu,
    game_screen,
    settings_screen,
    WIDTH,
    HEIGHT,
    start_button_rect,
    settings_button_rect,
)

pygame.init()

pygame.display.set_caption("Wolf3D Python")

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

#Виклик обробки гри
def main():
    while True:
        result = main_menu(screen, start_button_rect, settings_button_rect)
        if result == 'game':
            game_screen(screen)
        elif result == 'settings':
            settings_screen(screen)
        else:
            exit()

#Запуск файлу, як головного
if __name__ == "__main__":
    main()

#Завершення програми
pygame.quit()
sys.exit()
