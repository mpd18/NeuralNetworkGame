#import the pygame module, and the
#sys module for exiting the window we create
import pygame, sys, math, random

#import some useful constants
from pygame.locals import *

BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)

ROWS = 10
COLUMNS = 10
TILESIZE = 30
PEARMAX = 3
ROCKMAX = 3

class Player(object):
    
    def __init__(self,xy):
        self.x,self.y = xy
        print(xy)
        self.rect = pygame.rect.Rect((xy[0]*TILESIZE,xy[1]*TILESIZE,TILESIZE,TILESIZE))
        
    def handleMovement(self,objects):
        key = pygame.key.get_pressed()
        
        x = objects["player"][0]
        y = objects["player"][1]
        
        if key[pygame.K_LEFT] and self.rect.left > 0:
           objects["player"] = (x - TILESIZE, y - TILESIZE)
        if key[pygame.K_RIGHT] and self.rect.right < COLUMNS*TILESIZE:
           objects["player"] = (x + TILESIZE, y + TILESIZE)
           
    def draw(self):
        self.rect.x = self.y * TILESIZE
        self.rect.y = self.x * TILESIZE
        pygame.draw.rect(screen, BLUE, self.rect)
        
class Rock(object):

    def __init__(self,xy,id=None):
        self.id = id
        self.x,self.y = xy
        self.rect = pygame.rect.Rect((self.x*TILESIZE,self.y*TILESIZE,TILESIZE,TILESIZE))
        
    def fall(self,tiles):
        self.rect.move_ip(0,-10)
        
    def draw(self,params):
        pygame.draw.rect(screen, RED, self.rect)

class Pear(object):

    def __init__(self,xy,id=None):
        self.id = id
        self.x,self.y = xy
        self.rect = pygame.rect.Rect((self.x,self.y,TILESIZE,TILESIZE))
        
    def fall(self,tiles):
        self.rect.move_ip(0,-10)
        
    def draw(self,params):
        pygame.draw.rect(screen, GREEN, self.rect)
        
class BackgroundTile(object):

    def __init__(self,xy,id=None):
        self.id = id
        self.x,self.y = xy
        self.rect = pygame.rect.Rect((self.x,self.y,TILESIZE,TILESIZE))
        
    def draw(self):
        pygame.draw.rect(screen, WHITE, self.rect)
        
class GameTiles():

    def __init__(self):
        #initiating the game tiles
        self.tiles = []
        x = 0
        y = 0
        for i in range(ROWS):
            row = []
            for j in range(COLUMNS):
                tile = BackgroundTile((x,y))
                row.append(tile)
                x += TILESIZE
            x = 0
            y += TILESIZE
            self.tiles.append(row)
        
        self.playerPosition = None
        self.rockPosition = [None] * ROCKMAX
        self.pearPosition = [None] * PEARMAX
        
    def addPear(self):
        column = random.randint(0,19)
        
    def addRock(self):
        pass
        
    def addPlayer(self):
        self.tiles[ROWS-1][math.ceil(COLUMNS/2)] = Player((ROWS-1,math.ceil(COLUMNS/2)))
        self.playerPosition = (ROWS-1,math.ceil(COLUMNS/2))
        
    def movePlayer(self,direction):
        row,column = self.playerPosition
        #left
        if direction == 0 and column > 0:
            self.tiles[row][column].y -= 1
            self.swapTiles((row,column),(row,column-1))
            self.playerPosition = (row,column - 1)
            print(self.tiles[row][column].x,self.tiles[row][column].y)
        #right
        if direction == 1 and column < COLUMNS-1:
            self.tiles[row][column].y += 1
            self.swapTiles((row,column),(row,column + 1))
            self.playerPosition = (row,column + 1)
            print(self.tiles[row][column].x,self.tiles[row][column].y)
        
    def swapTiles(self,xy1,xy2):
        x1,y1 = xy1
        x2,y2 = xy2
        print(xy1)
        print(xy2)
        self.tiles[x1][y1], self.tiles[x2][y2] = self.tiles[x2][y2], self.tiles[x1][y1]
        
        
    def draw(self):
        for i in range(ROWS):
            for j in range(COLUMNS):
                object = self.tiles[i][j]
                object.draw()
                    
class Game(object):

    def __init__(self):
        self.tiles = GameTiles()
        
    #def timeStep(self):
    #    for rock in 
                    

#flow of upating tiles
"""
1. get input from keyboard
2. update object positions
3. update game tiles
"""
        
if __name__ == "__main__":
    #initialise the pygame module
    pygame.init()

    #create a new drawing surface, width=300, height=300
    screen = pygame.display.set_mode((ROWS*TILESIZE,COLUMNS*TILESIZE))
    #give the window a caption
    pygame.display.set_caption('Pear Catch')

    clock = pygame.time.Clock()
    
    tiles = GameTiles()
    tiles.addPlayer()
    #loop forever
    while True:

        #get all the user events
        for event in pygame.event.get():
            #if the user wants to quit
            if event.type == QUIT:
                #end the game and close the window
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print("moving left")
                    tiles.movePlayer(0)
                elif event.key == pygame.K_RIGHT:
                    print("moving right")
                    tiles.movePlayer(1)
                
        tiles.draw()
        #update the display        
        pygame.display.update()
        
        clock.tick(20)
        