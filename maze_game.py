import pyautogui
import pygame
import time
import random
import maze
import ball
import buttons
pygame.init()
pygame.font.init()
w, h = pyautogui.size()
h -= 65
WIDTH = w
HEIGHT = h


# Define colours
WHITE = (255, 255, 255)
GREEN = (0, 255, 0,)
PURPLE = (155, 48, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Game")
screen.fill((138,43,226))

g=970
h=930
pygame.draw.polygon(screen,(255,255,255),((g,h),(g+10,h),(g+10,h+20),(g+20,h+20),(g+20,h),(g+30,h),(g+15,h-20)))
font=pygame.font.SysFont('monospace', 20)
message=font.render('This is end point ',1,(0,0,0))
screen.blit(message,(1000,930))
buttons.create_button(screen)
maze.build_grid(screen)
maze.carve_out_maze(screen, 200, 100)

# ##### pygame loop #######
running = True
while running:
    # keep running at the at the right speed
    # process input (events)
    for event in pygame.event.get():
        # check for closing the window
        if event.type == pygame.QUIT:
            running = False
        press = pygame.key.get_pressed()
        if press[pygame.K_RIGHT] or press[pygame.K_LEFT] or press[pygame.K_UP] or press[pygame.K_DOWN]:
                ball.ball_mover(screen, press)
        if event.type==pygame.MOUSEBUTTONDOWN:
            m,n=event.pos
            btnnum=buttons.button_click(m,n)
            if btnnum==1:
                maze.build_grid(screen)
                maze.carve_out_maze(screen, 200, 100)
                ball.ball_reseter()
            if btnnum==2:
                maze.show_hint(screen)
            if btnnum==3:
                maze.show_solution(screen)
            if btnnum==4:
                pygame.quit()
    pygame.display.update()
