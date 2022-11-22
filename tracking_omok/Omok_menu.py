import pygame
import Omok_play as Op

# Screen Set
pygame.init()
screen_title = '오목 (흑) made by 규민'
screen_width = 950
screen_height = 950
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(screen_title)
screen_icon = pygame.image.load('image/Omok_icon.png')
pygame.display.set_icon(screen_icon)

bg = pygame.transform.scale(pygame.image.load("image/background.png"), (screen_width, screen_height))
button_mouse = pygame.transform.scale(pygame.image.load("image/button.png"), (450, 150))
button_hand = pygame.transform.scale(pygame.image.load("image/button.png"), (450, 150))
button_eyes = pygame.transform.scale(pygame.image.load("image/button.png"), (450, 150))

woodFont50 = pygame.font.Font( "font/drifttyp.ttf", 100, bold=True)
woodFont100 = pygame.font.Font( "font/drifttyp.ttf", 200, bold=True)
woodFont25 = pygame.font.Font( "font/drifttyp.ttf", 80, bold=True)

pygame.mixer.music.load('sound/bgm.mp3')
pygame.mixer.music.play(-1)

color = (255, 255, 175)

sub_title = woodFont50.render("Tracking", True, color)
main_title = woodFont100.render("Omok", True, color)
text_mouse = woodFont25.render("Mouse", True, color)
text_hand = woodFont25.render("Hand", True, color)
text_eyes = woodFont25.render("Eyes", True, color)

running = True
while running:
    screen.blit(bg, (0,0))
    bm = screen.blit(button_mouse, (250, 400))
    bh = screen.blit(button_hand, (250, 550))
    be = screen.blit(button_eyes, (250, 700))

    screen.blit(text_mouse, (335, 435))
    screen.blit(text_hand, (375 ,585))
    screen.blit(text_eyes, (375, 735))

    screen.blit(sub_title, (230, 100))
    screen.blit(main_title, (200, 200))

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            click_pos = pygame.mouse.get_pos()
            if bm.collidepoint(click_pos,):
                Op.run('mouse', True)
            if bh.collidepoint(click_pos):
                Op.run('hand', True)
            if be.collidepoint(click_pos):
                Op.run('eyes', True)
    pygame.display.update()
pygame.quit()