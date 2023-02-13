import pygame
pygame.font.init()
pygame.init()
COLOR=(0,0,0)
font=pygame.font.SysFont('monospace',37)

t1=font.render('RESTART', 1,COLOR)
t2=font.render('HINT',1,COLOR)
t3=font.render('SOLUTION',1,COLOR)
t4=font.render('QUIT',1,COLOR)

r1=pygame.Rect(1300,150,200,70)
r2=pygame.Rect(1300,350,200,70)
r3=pygame.Rect(1300,550,200,70)
r4=pygame.Rect(1300,750,200,70)

def create_button(screen):
      pygame.draw.rect(screen,(124	,252	,0),r1)
      pygame.draw.rect(screen,(124	,252	,0),r2)
      pygame.draw.rect(screen,(124	,252	,0),r3)
      pygame.draw.rect(screen,(124	,252	,0),r4)
      screen.blit(t1,(1320,160))
      screen.blit(t2,(1355,360))
      screen.blit(t3,(1310,560))
      screen.blit(t4,(1355,760))

def button_click(x,y):
      if r1.collidepoint(x, y):
            return 1
      if r2.collidepoint(x,y):
            return 2
      if r3.collidepoint(x,y):
            return 3
      if r4.collidepoint(x,y):
            return 4
      return 5


