import pygame
from solver import solve, valid
import time 
pygame.font.init()


class Grid:
    #fix this board to get random board
    board = [
        [7,8,0,4,0,0,1,2,0],
        [6,0,0,0,7,5,0,0,9],
        [0,0,0,6,0,1,0,7,8],
        [0,0,7,0,4,0,2,6,0],
        [0,0,1,0,5,0,9,3,0],
        [9,0,4,0,6,0,0,0,5],
        [0,7,0,3,0,0,0,1,2],
        [1,2,0,0,0,7,4,0,0],
        [0,4,9,2,0,6,0,0,7]
    ]

    #constructor for the grid
    def __init__(self, rows, cols, width, height):
        self.rows = rows
        self.cols = cols
        self.cubes = [[Cube(self.board[i][j], i, j, width, height) for j in range(cols)] for i in range (rows)]
        self.width = width
        self.height = height
        self.model = None
        self.selected = None

    #updating the current modal
    def upate_modal(self):
        pass

    #writing on the board
    def place(self, val):
        pass

    #writing the temp val on the board
    def sketch(self, val):
        pass

    #drawing the grid 
    def draw(self, win):
        pass

    #selecting the specific box
    def select(self, row, col):
        pass

    #clear the slected box
    def clear(self):
        pass

    #selecting hte specific box
    def click(self, pos):
        pass

    #game over
    def is_finished(self):
        pass


#class for each ubsided box
class Cube:
    #init values
    rows = 9
    cols = 9

    #grid constructor
    def __init__(self, value, row, col, width, height):
        self.value = value
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.selected = False

    #draw the board
    def draw(self, win):
        #drawing the game
        fnt = pygame.font.SysFont("comicsans", 40) #set font
        
        #setting the distance apart
        gap = self.width / 9
        x = self.col * gap
        y = self.row * gap

        if self.temp != 0 and self.value == 0:
            text = fnt.render(str(self.temp), 1, (128,128,128))
            win.blit(text, (x+5, y+5))
        elif not(self.value == 0):
            text = fnt.render(str(self.value), 1, (0,0,0))
            win.blit(text, (x + (gap/2 - text.get_width()/2), y + (gap/2 - text.get_height()/2)))

        if self.selected:
            pygame.draw.rect(win, (255,0,0), (x,y,gap,gap), 3)     

    #set the currentvalue for the value
    def set(self, val):
        self.value = val

    #ssetting the temp value
    def set_temp(self, val):
        self.temp = val

#drawing the window
def redraw_window(win, board, time, strikes):
    win.fill((255,255,255))
    #draw time
    fnt = pygame.font.SysFont("comicsans", 40)
    win.blit(text, (540 - 160, 560))

    #drawing the x's
    text = fnt.render("X " * strikes, 1, (255, 0, 0))
    win.blit(text, (20, 560))
    #draw the board
    board.draw(win)

#timing 
def format_time(secs):
    sec = secs%60
    minute = secs//60
    hour = minute//60
#start game