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
        pass

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
    def __init__9(self, value, row, col, width, height):
        pass

    #draw the board
    def draw(self, win):
        pass

    #set the currentvalue for the value
    def set(self, val):
        pass

    #ssetting the temp value
    def set_temp(self, val):
        pass

