import pygame

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load('Щорс.mp3')
pygame.mixer.music.play(-1)

WIDTH = 800
HEIGHT = 600

image = pygame.image.load("Mayak.jpg")
image = pygame.transform.scale(image, (800, 600))

#Перемінна для шрифта і кнопок
font = pygame.font.SysFont("Arial", 40)

#Перемінні для кнопок
button_color = (255, 100, 100)
button_hover_color = (255, 150, 150)
button_width = 300
button_height = 60
start_button_rect = pygame.Rect(WIDTH // 2 - button_width // 2, HEIGHT // 2 - 100, button_width, button_height)
settings_button_rect = pygame.Rect(WIDTH // 2 - button_width // 2, HEIGHT // 2 + 20, button_width, button_height)

#Створюю кнопки
def draw_button(screen, rect, text):
    pygame.draw.rect(screen, button_color, rect)
    pygame.draw.rect(screen, (0, 0, 0), rect, 3)
    label = font.render(text, True, (0, 0, 0))
    screen.blit(label, (rect.x + (rect.width - label.get_width()) // 2, rect.y + (rect.height - label.get_height()) // 2))

#Універсальна функція для забарвлення екрану
def handle_screen_events(screen, color):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(color)
        pygame.display.flip()

#Функція для безперебійної обробки гри
def main_menu(screen, start_button_rect, settings_button_rect):
    running = True
    while running:
        screen.fill((30, 30, 30))
        screen.blit(image, (0, 0))

        #Обробка подій
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button_rect.collidepoint(event.pos):
                    print("Початок гри!")
                    game_screen(screen)
                elif settings_button_rect.collidepoint(event.pos):
                    print("Перехід до налаштувань!")
                    settings_screen(screen)

        #Виклик кнопок
        draw_button(screen, start_button_rect, "Почати гру")
        draw_button(screen, settings_button_rect, "Налаштування")

        #Малюю екран, переводжу із заднього буферу
        pygame.display.flip()

#Створення зеленого екрану
def game_screen(screen):
    handle_screen_events(screen, (0, 255, 0))

#Створення синього екрану
def settings_screen(screen):
    handle_screen_events(screen, (100, 100, 255))

