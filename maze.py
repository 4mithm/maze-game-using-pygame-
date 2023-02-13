import pygame
import random
import time
pygame.init()
m = n = 21
w = 40
grid = []
visited = []
stack = []
solution = {}
solutionstack=[]
# ----------------------------------------------
WHITE = (255, 255, 255)
GREEN = (0, 255, 0,)
PURPLE = (155, 48, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
ball_x = 207
ball_y = 107

def build_grid(screen):
    global grid
    grid=[]
    w = 40
    y = 60
    for i in range(1, m):
      # set x coordinate to start position
        x = 200
        # start a new row
        y = y + 40
        for j in range(1, n):
            pygame.draw.line(screen, WHITE, [x, y], [
                x + w, y], 4)           # top of cell
            # right of cell
            pygame.draw.line(screen, WHITE, [x + w, y], [x + w, y + w], 4)
            # bottom of cell
            pygame.draw.line(screen, WHITE, [x + w, y + w], [x, y + w], 4)
            # left of cell
            pygame.draw.line(screen, WHITE, [x, y + w], [x, y], 4)
            # add cell to grid list
            grid.append((x, y))
            # move cell to new position
            x = x + 40


l_paint = 40-3
b_paint = 80-3
gap = 3


def push_up(screen, x, y):
    # draw a rectangle twice the width of the cell
    pygame.draw.rect(screen, PURPLE, (x + gap, y - w + gap, l_paint, b_paint), 0)
    # to animate the wall being removed
    pygame.display.update()


def push_down(screen, x, y):
    pygame.draw.rect(screen, PURPLE, (x + gap, y + gap, l_paint, b_paint), 0)
    pygame.display.update()


def push_left(screen, x, y):
    pygame.draw.rect(screen, PURPLE, (x - w + gap, y + gap, b_paint, l_paint), 0)
    pygame.display.update()


def push_right(screen, x, y):
    pygame.draw.rect(screen, PURPLE, (x + gap, y + gap, b_paint, l_paint), 0)
    pygame.display.update()


def carve_out_maze(screen, x, y):
    global stack
    global visited
    global solution
    global solutionstack
    solutionstack=[]
    solution={}
    visited=[]
    stack=[]
    stack.append((x, y))
    # add starting cell to visited list
    visited.append((x, y))
    while len(stack) > 0:
      # loop until stack is empty
      # slow program now a bit
        cell = []                                                  # define cell list
        if (x - w, y) not in visited and (x - w, y) in grid:       # left cell available?
            cell.append("left")

        if (x, y + w) not in visited and (x, y + w) in grid:     # down cell available?
            cell.append("down")

        if (x, y - w) not in visited and (x, y - w) in grid:      # up cell available?
            cell.append("up")

        if (x + w, y) not in visited and (x + w, y) in grid:       # right cell available?
            # if yes add to cell list
            cell.append("right")

        # check to see if cell list is empty
        if len(cell) > 0:
            # select one of the cell randomly
            cell_chosen = random.choice(cell)
            # (random.choice(cell))

            if cell_chosen == "right":                             # if this cell has been chosen
                # call push_right function
                push_right(screen, x, y)
                # solution = dictionary key = new cell, other = current cell
                solution[(x + w, y)] = x, y
                x = x + w                                          # make this cell the current cell
                # add to visited list
                visited.append((x, y))
                # place current cell on to stack
                stack.append((x, y))

            elif cell_chosen == "left":
                push_left(screen, x, y)
                solution[(x - w, y)] = x, y
                x = x - w
                visited.append((x, y))
                stack.append((x, y))

            elif cell_chosen == "down":
                push_down(screen, x, y)
                solution[(x, y + w)] = x, y
                y = y + w
                visited.append((x, y))
                stack.append((x, y))

            elif cell_chosen == "up":
                push_up(screen, x, y)
                solution[(x, y - w)] = x, y
                y = y - w
                visited.append((x, y))
                stack.append((x, y))
        else:
            # if no cells are available pop one from the stack
            x, y = stack.pop()
    pygame.draw.rect(screen, RED, (ball_x, ball_y, 30, 30), 0)
    a,b=960,860
    while (a,b)!=(200,100):
        a,b = solution[a,b]
        solutionstack.append((a,b))

def show_solution(screen):
    for m,n in solutionstack:
        pygame.draw.rect(screen, YELLOW, (m+15, n+15, 10,10), 0,border_radius=5)

def show_hint(screen):
    for _ in range(10):
        o,p=random.choice(solutionstack)
        pygame.draw.rect(screen, YELLOW, (o+15, p+15, 10,10), 0,border_radius=5)




    
