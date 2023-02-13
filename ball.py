import pygame
pygame.font.init()
pygame.init()
ball_x = 207
ball_y = 107
ball_w = 1
WHITE = (255, 255, 255)
GREEN = (0, 255, 0,)
PURPLE = (155, 48, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
color = (255, 255, 255, 255)
def ball_reseter():
      global ball_x
      global ball_y
      ball_x=207
      ball_y=107

def ball_mover(screen, press):
    global ball_x
    global ball_y
    winx, winy = screen.get_size()
    if ball_x+30 >= winx or ball_y+30 >= winy or ball_x-30 <= 0 or ball_y-30 <= 0:
        return
    else:
      
        i = 0
        while i < 30:
            if ball_x>=960 and ball_y>=860:
                  winner_print(screen)
                  return 
            pygame.draw.rect(screen, PURPLE, (ball_x, ball_y, 30, 30), 0)
            if press[pygame.K_RIGHT] and not white_check(screen, ball_x, ball_y, 'r'):
                ball_x += 1
            if press[pygame.K_LEFT] and not white_check(screen, ball_x, ball_y, 'l'):
                ball_x -= 1
            if press[pygame.K_DOWN] and not white_check(screen, ball_x, ball_y, 'd'):
                ball_y += 1
            if press[pygame.K_UP] and not white_check(screen, ball_x, ball_y, 'u'):
                ball_y -= 1
            pygame.draw.rect(screen, RED, (ball_x, ball_y, 30, 30), 0)
            i += 1


def white_check(screen, x, y, d):
    if d == 'd':
        y += 31
    elif d == 'u':
        y -= 1
    elif d == 'l':
        x -= 1
    elif d == 'r':
        x += 31
    if d == 'd' or d == 'u':
        for i in range(31):
            if screen.get_at((x+i, y)) == color:
                return True
        return False
    if d == 'l' or d == 'r':
        for i in range(31):
            if screen.get_at((x, y+i)) == color:
                return True
        return False
def winner_print(screen):
      font=pygame.font.SysFont('monospace',190,bold=True)
      t1=font.render("YOU WON", 1, (0,245	,255))
      screen.blit(t1,(200,400))