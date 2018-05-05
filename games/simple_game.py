#import the pygame module, and the
#sys module for exiting the window we create
import pygame, sys, math

#import some useful constants
from pygame.locals import *

BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)

ROWS = 20
COLUMNS = 20
TILESIZE = 60

class Player(object):
    
    def __init__(self):
        self.rect = pygame.rect.Rect((150,270,TILESIZE,TILESIZE))
        
    def handleMovement(self,objects):
        key = pygame.key.get_pressed()
        
        x = objects["player"][0]
        y = objects["player"][1]
        
        if key[pygame.K_LEFT] and self.rect.left > 0:
           objects["player"] = (x - TILESIZE, y-TILESIZE)
        if key[pygame.K_RIGHT] and self.rect.right < COLUMNS*TILESIZE:
           objects["player"] = (x + TILESIZE, y + TILESIZE)
           
    def draw(self,objects):
        self.rect.x = xy[0]
        self.rect.y = xy[1]
        pygame.draw.rect(screen, BLUE, self.rect)
        
class Rock(object):
    def __init__(self,params):
        self.rect = pygame.rect.Rect(params)
    def fall(self,tiles):
        self.rect.move_ip(0,-10)
    def draw(self,params):
        pygame.draw.rect(screen, RED, self.rect)

class Pear(object):
    def __init__(self,column,tiles):
        self.rect = pygame.rect.Rect(params)
    def fall(self,tiles):
        self.rect.move_ip(0,-10)
    def draw(self,params):
        pygame.draw.rect(screen, GREEN, self.rect)
        
class backgroundTile(object):
    def __init__(self,params):
        self.rect = pygame.rect.Rect((params[0],params[1],TILESIZE,TILESIZE))
    def draw(self,objects):
        pygame.draw.rect(screen, WHITE, self.rect)
        
class Objects(object):
    def __init__(self):
        self.positions = {"rocks" : [], "pears" : [], "player" = (ROWS-1,math.floor(COLUMNS/2))}
        
class GameTiles():
    def __init__(self):
        #initiating the game tiles
        self.tiles = []
        x = 0
        y = 0
        for i in range(ROWS):
            row = []
            for j in range(COLUMNS):
                tile = backgroundTile((x,y))
                row.append(tile)
                x += TILESIZE
            x = 0
            y += TILESIZE
            self.tiles.append(row)
            
    def draw(self,objects):
        for i in range(ROWS):
            for j in range(COLUMNS):
                self.tiles[i][j].draw(objects)
        
if __name__ == "__main__":
    #initialise the pygame module
    pygame.init()

    #create a new drawing surface, width=300, height=300
    screen = pygame.display.set_mode((ROWS*TILESIZE,COLUMNS*TILESIZE))
    #give the window a caption
    pygame.display.set_caption('Pear Catch')

    clock = pygame.time.Clock()

    #create player square
    player = Player()
    
    tiles = GameTiles()
    #loop (repeat) forever
    while True:

        #get all the user events
        for event in pygame.event.get():
            #if the user wants to quit
            if event.type == QUIT:
                #end the game and close the window
                pygame.quit()
                sys.exit()
                
        tiles.draw()
        #update the display        
        pygame.display.update()
        
        clock.tick(20)
        