def run(tracking_type, high_quality):
    import pygame
    import random as r
    import time as t
    import Omok_mouse as mouse
    import Omok_function as OF
    
    # Screen Set
    pygame.init()
    screen_title = '오목 (흑) made by 규민'
    screen_width = 950
    screen_height = 950
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption(screen_title)
    screen_icon = pygame.image.load('image/Omok_icon.png')
    pygame.display.set_icon(screen_icon)

    # Background Music Set
    put_stone = pygame.mixer.Sound("sound/put_stone.mp3")
    pygame.mixer.music.load('sound/bgm.mp3')
    pygame.mixer.music.play(-1)

    # Color
    Black = (0, 0, 0)
    White = (255, 255, 255)
    Green = (0, 255, 0)
    Yellow = (255, 255, 175)

    # Omok board Set / pygame
    OmokBoard = []
    OmokBoardPut = []
    for fy in range(15):
        OmokBoard.append([])
        OmokBoardPut.append([])
        for fx in range(15):
            OmokBoard[-1].append(pygame.Rect(0, 0, 50, 50))
            OmokBoard[fy][fx].center = (125 + fx * 50, 125 + fy * 50)
            OmokBoardPut[-1].append(0)
    bg = pygame.transform.scale(pygame.image.load("image/background.png"), (screen_width, screen_height))
    box = pygame.image.load('image/box.png')
    black_stone = pygame.image.load('image/black_stone.png')
    white_stone = pygame.image.load('image/white_stone.png')
    forbidden = pygame.image.load('image/forbidden.png')

    woodFont50 = pygame.font.Font( "font/drifttyp.ttf", 100, bold=True)

    black_win = woodFont50.render("You are win!", True, Black)
    white_win = woodFont50.render("You are lose!", True, Black)

    # Play
    running = True
    cx, cy = 0, 0
    while running:
        ## Omok board Set
        # Background Color Set
        screen.blit(bg, (0,0))

        # Rect
        for fy in range(14):
            for fx in range(14):
                screen.blit(box, (125 + fx * 50, 125 + fy * 50))
                pygame.draw.rect(screen, Yellow, (125 + fx * 50, 125 + fy * 50, 50, 50), 1)

        # Edge, Small circle
        pygame.draw.rect(screen, Yellow, (125, 125, 700, 700), 2)
        for i in ((275, 275), (675, 275), (475, 475), (275, 675), (675, 675)):
            pygame.draw.circle(screen, Yellow, i, 8)
        
        # Stone Reset
        for fy in range(15):
            for fx in range(15):
                if OmokBoardPut[fy][fx] == 1:
                    pygame.draw.circle(screen, Yellow, OmokBoard[fy][fx].center, 23)
                    screen.blit(black_stone, (105 + fx * 50, 105 + fy * 50))
                elif OmokBoardPut[fy][fx] == 2:
                    pygame.draw.circle(screen, Yellow, OmokBoard[fy][fx].center, 22)
                    screen.blit(white_stone, (105 + fx * 50, 105 + fy * 50))
                else:
                    if not OF.get_information_stone(OmokBoardPut, fx, fy, 1) and high_quality:
                        screen.blit(forbidden, (100 + fx * 50, 100 + fy * 50))
        
        ## Omok board Set

        ## Click Process
        click_bool, cx, cy = mouse.get_mouse(tracking_type)
        
        if tracking_type == 'mouse':
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click_bool = True

        # Draw Click Pos
        pygame.draw.circle(screen, Green, OmokBoard[cy][cx].center, 5)
        if click_bool and OmokBoardPut[cy][cx] == 0:
            res = OF.get_information_stone(OmokBoardPut, cx, cy, 1)
            if res:
                OmokBoardPut[cy][cx] = 1
                pygame.draw.circle(screen, Yellow, OmokBoard[cy][cx].center, 22)
                screen.blit(black_stone, (105 + cx * 50, 105 + cy * 50))
                pygame.mixer.Sound.play(put_stone)
                if res == 2:
                    screen.blit(black_win, (75, 20))
                    running = False
                vxy = []
                vMax = 3
                for by in range(15):
                    for bx in range(15):
                        if OmokBoardPut[by][bx] != 0:
                            continue
                        vTmp = OF.get_value_stone(OmokBoardPut, bx, by)
                        if vTmp > vMax:
                            vMax = vTmp
                            vxy = []
                        if vTmp == vMax:
                            vxy.append((bx, by))
                bx, by = r.choice(vxy)
                OmokBoardPut[by][bx] = 2
                pygame.draw.circle(screen, Yellow, OmokBoard[by][bx].center, 22)
                screen.blit(white_stone, (105 + bx * 50, 105 + by * 50))
                if OF.get_information_stone(OmokBoardPut, bx, by, 2) == 2:
                    screen.blit(white_win, (75, 20))
                    running = False
                print(bx, by, vMax)
                # t.sleep(1)
        pygame.display.update()
        t.sleep(0.01)
    t.sleep(5)
    pygame.quit()