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
        self.model = [[self.cubes[i][j].value for j in range(sef.cols)] for i in range(self.rows)]

    #writing on the board
    def place(self, val):
        row, col = self.selected
        if self.cubes[row][col].value == 0:
            self.cues[row][col].set(val)
            self.update_modal()

            if valid(self.model, val, (row,col)) and solve(self.model):
                return True
            else:
                self.cubes[row][col].set(0)
                self.cubes[row][col].set_temp(0)
                self.update_modal()
                return False


    #writing the temp val on the board
    def sketch(self, val):
        row, col = self.selected
        self.cubes[row][col].set_temp(val)
        

    #drawing the grid 
    def draw(self, win):
        #grid lines
        gap = self.width / 9
        for i in range(self.rows+1):
            if i % 3 == 0 and i != 0:
                thick = 4
            else:
                thick = 1

            pygame.draw.line(win, (0,0,0), (0, i*gap), (self.width, i*gap), thick)
            pygame.draw.line(win, (0, 0, 0), (i * gap, 0), (i * gap, self.height), thick)
    
        #drawing cubes
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].draw(win)

    #selecting the specific box
    def select(self, row, col):
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].draw(win)

    #clear the slected box
    def clear(self):
        row, col = self.selected
        if self.cubes[row][col].value == 0:
            self.cubes[row][col].set_temp(0)


    #selecting hte specific box
    def click(self, pos):
        #find the position on the board
        if pos[0] < self.width and pos[1] < self.height:
            gap = self.width / 9
            x = pos[0]
            y = pos[1]
            return (int(y), int(x))
        return None

    #game over
    def is_finished(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.cubes[i][j] == 0:
                    return False


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